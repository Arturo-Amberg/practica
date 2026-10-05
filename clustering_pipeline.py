def classify_mining_valleys(data):
    if data is None:
        raise ValueError("No geospatial data provided")
    
    print("Starting classification...")
    
    # Upgraded to handle spatial density
    import hdbscan
    model = hdbscan.HDBSCAN(min_cluster_size=5)
    results = model.fit_predict(data)
    
    return results