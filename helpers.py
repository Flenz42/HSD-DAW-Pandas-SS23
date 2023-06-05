def filter_other(data, threshold_pct=0.03):
    total = sum(data)
    print(total)
    threshold_abs = threshold_pct * total
    filtered_data = data.loc[data >= threshold_abs]
    excluded_data = data.loc[data < threshold_abs]
    total_excluded = sum(excluded_data)
    filtered_data['Other'] = total_excluded
    return filtered_data

def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{:.1f}%\n({v:d})'.format(pct, v=val)
    return my_format