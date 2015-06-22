import numpy as np

def boxcar_smooth(in_data, in_days, window=1):
    """
    Calculates exponentially filtered time series using
    a boxcar filter - basically a moving average calculation

    Parameters
    ----------
    in_data : double numpy.array
        input data
    in_jd : double numpy.array
        julian dates of input data
    window : int
        characteristic time used for calculating
        the weight
    nan : double
        nan values to exclude from calculation
    """
    filtered = np.empty(len(in_data))

    filtered.fill(np.nan)

    for i in range(in_days.shape[0]):
        sum = 0
        nobs = 0
        for j in range(in_days.shape[0]):
            tdiff = in_days[j] - in_days[i]
            if abs(tdiff) <= window/2:
                sum = sum + in_data[j]
                nobs = nobs + 1

        filtered[i] = sum/nobs

    return filtered

if __name__ == '__main__':
    ts_values = np.random.rand(10000)
    ts_days = np.sort(np.random.rand(10000) * 365 )
    smoothed = boxcar_smooth(ts_values, ts_days, window=25)
