def linear_regression_least_squares(samples, dim=2):
    ''' samples Interleaved list of sample coordinates
        dim Number of dimensions of list
    '''
    n = len(samples)
    
    print samples
    
    print n, "samples"
    epsilons = [[] for i in range(dim)]
    print epsilons
    epsilon_product = []
    
    mean = [sum(zip(*samples)[i])/float(n) for i in range(dim)]
    
    print mean
    
    for i in range(n):
        product = 1
        
        for j in range(0, dim):
            print samples[i]
            epsilons[j].append(samples[i][j]-mean[j])
            print epsilons
            product *= epsilons[j][i]
        
        products = [[reduce(lambda x, y: x*y, epsilons[j]) for j in range(dim)] for i in range(dim) if i!=j]
        print products
  
        epsilon_product.append(product)
    
    #area of square x^2
    #surface area of cuboid 2 (x_1 x_2) + 2 (x_1 x_3) + 2 (x_2 x_3)
    #surface area n sum i=0 product 2 {x_n/x_i}
    #volume of cuboid x_1 x_2 x_3 i.e. product x_i
    
    
    
    #using sample std dev. w/ Bessel's correction
    sd = [[pow(sum([pow(epsilons[i][j], 2) for j in range(n)])/(n-1), 0.5)] for i in range(dim)]
    
    print sd
    
    
    sd_product = reduce( lambda x, y: x*y, sd[i] )
    print sd_product
    r = (sum(epsilon_product)/(sd_product))/(n-1)
    print r
    
    
    #pearson
    #az
    #bz
    #product / sqrt(prod(sum(x_i^2
    
    rslope=r*sd[1][0]/sd[0][0]
    print rslope
    #mention of Pedhazur
    #r(sx/sy)
    #sum(epsilon_product)/n(sx*sy) (sy/sx)
    #y std dev's cancel out
    #sum(epsilon_product)/n(epsilon_x^2/n)
    #n cancels out
    #sum(epsilon_product)/epsilon_x^2
    slope = sum(epsilon_product)/sum([epsilons[0][i]**2 for i in range(n)])
    
    intercept = mean[1]-slope*mean[0] 
    
    return (intercept, slope)