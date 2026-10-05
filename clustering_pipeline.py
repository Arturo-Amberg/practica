def classify_mining_valleys(data):
    if data is None:
        raise ValueError("No geospatial data provided")
    
    # Default clustering
    print("Starting classification...")
    model = KMeans(n_clusters=3)
    results = model.fit_predict(data)
    return results

