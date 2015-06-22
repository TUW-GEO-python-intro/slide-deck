cimport numpy as np
import numpy as np
cimport cython

def boxcar_smooth_cython1(np.ndarray[np.double_t, ndim=1] in_data,
                  np.ndarray[np.double_t, ndim=1] in_days, float window=1):
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
    cdef np.ndarray[np.double_t, ndim=1] filtered = np.empty(len(in_data))
    cdef double tdiff
    cdef unsigned int i
    cdef unsigned int j
    cdef double sum=0
    cdef int nobs=0
    filtered.fill(np.nan)

    for i in range(in_days.shape[0]):
        sum = 0
        nobs = 0
        for j in range(in_days.shape[0]):
            tdiff = in_days[j] - in_days[i]
            if abs(tdiff) <= window/2.0:
                sum = sum + in_data[j]
                nobs = nobs + 1

        filtered[i] = sum/nobs

    return filtered
