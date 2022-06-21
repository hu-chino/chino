import numpy as np


def interpolate(time, value, frequency, n_dft, threshold=1.0*10**8):
    """ALSによる照度データを0次補間したものを返す

    :param list<float> time: サンプリング時刻の時系列データ
    :param list<float> value: サンプリング値の時系列データ
    :param float frequency: ALSのサンプリング周波数
    :param int n_dft: dftに用いるデータ点数
    :param float threshold: 欠損したと判定する時刻の範囲の絶対値　
    :return: 補間後のデータ。(time, value)
    :rtype: 戻り値の型
    """
    T_s = 1 / frequency
    prev_time, prev_value = 0, -1

    processed = []
    for i in range(len(time)):
        if not prev_time or (time[i] - prev_time < threshold):
            processed.append((time[i], value[i]))
            prev_time, prev_value = time[i], value[i]
        else:
            times = round((time[i] - prev_time) / (10**9 / n_dft), 0)
            for j in range(int(times) - 1):
                processed.append(
                    (prev_time + (j + 1) * 10**9 * T_s, prev_value)
                )
            processed.append((time[i], value[i]))
            prev_time, prev_value = time[i], value[i]
    processed = np.array(processed)
    return processed
