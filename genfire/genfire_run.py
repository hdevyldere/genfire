import genfire as gf
path = '/home/hannah/Documents/Data/Xiaohui_NW/06272018_Pt/'
pars = dict(projections   =  path + "y4_short.mat",
            eulerAngles   =  path + "y2angles_short.mat",
            support       =  None,
            initialObject =  None,
            resultsFilename = path + "recon_y4_short_01.mrc",

            interpolationCutoffDistance  = .7,
            oversamplingRatio  =  1,
            resolutionExtensionSuppressionState =  1,  # 1) Turn on resolution extension/suppression, 2) No resolution extension/suppression, 3) Just resolution extension
            griddingMethod  =  "FFT",

            numIterations  =  20,
            calculateRfree  =  1,
            )

GF = gf.reconstruct.GenfireReconstructor(**pars)
results = GF.reconstruct()
gf.fileio.saveResults(results, GF.params.resultsFilename)

