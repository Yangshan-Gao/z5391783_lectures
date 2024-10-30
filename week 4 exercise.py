    df = yf.download(tic, start=start, end=end)
    df.to_csv(pth)

print('Yangshan Gao, z5391783')

if __name__ == "__main__":
    import os
    import toolkit_config as cfg
    tic = 'WES.AX'
    pth = os.path.join(cfg.DATADIR, 'wes_stk_prc.csv')
    yf_prc_to_csv(tic, pth)