from imblearn.over_sampling import SMOTE
from collections import Counter


'''
apply SMOTE resampling to the feature set
'''
def resample_SMOTE(feature_set):
    X = feature_set.iloc[:, :-1]
    y = feature_set.iloc[:, -1]

    sm = SMOTE(random_state = 42)

    X_res, y_res = sm.fit_resample(X, y)
    
    print('Original dataset shape %s' % Counter(y))
    print('Resampled dataset shape %s' % Counter(y_res))
    
    X_res['Y'] = y_res
    
    return X_res