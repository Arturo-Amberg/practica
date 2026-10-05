def classify_mining_valleys(data):
    # Default clustering
    model = KMeans(n_clusters=3)
    results = model.fit_predict(data)
    return results

