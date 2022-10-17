import matplotlib.pyplot as plt


def average(series):
    return float(sum(series))/len(series)
def moving_average(series, n):
    return average(series[-n:])
def weighted_average(series, weights):
    result = 0.0
    weights.reverse()
    for n in range(len(weights)):
        result += series[-n-1] * weights[n]
    return result

def exponential_smoothing(series, alpha):
    result = [series[0]] # first value is same as series
    for n in range(1, len(series)):
        result.append(alpha * series[n] + (1 - alpha) * result[n-1])
    return result
def double_exponential_smoothing(series, alpha, beta):
    result = [series[0]]
    for n in range(1, len(series)+1):
        if n == 1:
            level, trend = series[0], series[1] - series[0]
        if n >= len(series): # we are forecasting
          value = result[-1]
        else:
          value = series[n]
        last_level, level = level, alpha*value + (1-alpha)*(level+trend)
        trend = beta*(level-last_level) + (1-beta)*trend
        result.append(level+trend)
    return result

def initial_trend(series, slen):
    sum = 0.0
    for i in range(slen):
        sum += float(series[i+slen] - series[i]) / slen
    return sum / slen

def initial_seasonal_components(series, slen):
    seasonals = {}
    season_averages = []
    n_seasons = int(len(series)/slen)
    # compute season averages
    for j in range(n_seasons):
        season_averages.append(sum(series[slen*j:slen*j+slen])/float(slen))
    # compute initial values
    for i in range(slen):
        sum_of_vals_over_avg = 0.0
        for j in range(n_seasons):
            sum_of_vals_over_avg += series[slen*j+i]-season_averages[j]
        seasonals[i] = sum_of_vals_over_avg/n_seasons
    return seasonals
def triple_exponential_smoothing(series, slen, alpha, beta, gamma, n_preds):
    result = []
    seasonals = initial_seasonal_components(series, slen)
    for i in range(len(series)+n_preds):
        if i == 0: # initial values
            smooth = series[0]
            trend = initial_trend(series, slen)
            result.append(series[0])
            continue
        if i >= len(series): # we are forecasting
            m = i - len(series) + 1
            result.append((smooth + m*trend) + seasonals[i%slen])
        else:
            val = series[i]
            last_smooth, smooth = smooth, alpha*(val-seasonals[i%slen]) + (1-alpha)*(smooth+trend)
            trend = beta * (smooth-last_smooth) + (1-beta)*trend
            seasonals[i%slen] = gamma*(val-smooth) + (1-gamma)*seasonals[i%slen]
            result.append(smooth+trend+seasonals[i%slen])
    return result

series = [3,10,12,13,12,10,12]
weights = [0.1, 0.2, 0.3, 0.4]
promedio=average(series)
promedio_variable=moving_average(series,3)
promedio_ponderado=weighted_average(series,weights)
suavizamiento_exponencial=exponential_smoothing(series,0.1)
suavizamiento_exponencial2=exponential_smoothing(series,0.9)
suavizamiento_exponencial_doble=double_exponential_smoothing(series,0.9,0.1)
suavizamiento_exponencial_doble2=double_exponential_smoothing(series,0.9,0.9)
plt.figure()
plt.subplot(221)
plt.title('Predicción básica')
plt.plot(series,'bo-')
plt.plot(7,promedio,"go")
plt.annotate("promedio",xy=(7,promedio),
                        xytext=(7.2,promedio+0.2),
                        arrowprops=dict(arrowstyle="->"))
plt.plot(7,promedio_variable,"ro")
plt.annotate("promedio variable",xy=(7,promedio_variable),
                        xytext=(7.2,promedio_variable+0.2),
                        arrowprops=dict(arrowstyle="->"))
plt.plot(7,promedio_ponderado,"yo")
plt.annotate("promedio ponderado",xy=(7,promedio_ponderado),
                        xytext=(7.2,promedio_ponderado+1),
                        arrowprops=dict(arrowstyle="->"))
plt.subplot(222)
plt.title('Suavizamiento exponencial')
plt.plot(series,'bo-')
plt.plot(suavizamiento_exponencial,"mo")
plt.annotate("alpha 0.1",xy=(6,suavizamiento_exponencial[6]),
                        xytext=(6.2,suavizamiento_exponencial[6]+0.2),
                        arrowprops=dict(arrowstyle="->"))
plt.plot(suavizamiento_exponencial2,"yo")
plt.annotate("alpha 0.9",xy=(6,suavizamiento_exponencial2[6]),
                        xytext=(6.2,suavizamiento_exponencial2[6]+0.2),
                        arrowprops=dict(arrowstyle="->"))
plt.subplot(223)
plt.title('Suavizamiento exponencial doble')
plt.plot(series,'bo-')
plt.plot(suavizamiento_exponencial_doble,"co")
plt.annotate("beta 0.1",xy=(7,suavizamiento_exponencial_doble[7]),
                        xytext=(7.2,suavizamiento_exponencial_doble[7]+0.2),
                        arrowprops=dict(arrowstyle="->"))
plt.plot(suavizamiento_exponencial_doble2,"ro")
plt.annotate("beta 0.9",xy=(7,suavizamiento_exponencial_doble2[7]),
                        xytext=(7.2,suavizamiento_exponencial_doble2[7]+0.2),
                        arrowprops=dict(arrowstyle="->"))
series = [30,21,29,31,40,48,53,47,37,39,31,29,17,9,20,24,27,35,41,38,
          27,31,27,26,21,13,21,18,33,35,40,36,22,24,21,20,17,14,17,19,
          26,29,40,31,20,24,18,26,17,9,17,21,28,32,46,33,23,28,22,27,
          18,8,17,21,31,34,44,38,31,30,26,32]
plt.subplot(224)
plt.title('Suavizamiento exponencial triple')
plt.plot ( series,"bo-")
plt.plot (triple_exponential_smoothing(series, 12, 0.7, 0.02, 0.9, 24))
plt.show()
