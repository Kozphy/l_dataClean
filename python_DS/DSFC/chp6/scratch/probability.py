def inverse_normal_cdf(
    p: float, mu: float = 0, sigma: float = 1, tolerance: float = 0.00001
) -> float:
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
