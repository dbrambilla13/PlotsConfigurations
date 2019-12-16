# variables

#variables = {}

#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow

# variables['events']  = {   'name': '1',
# 'range' : (1,0,2),
# 'xaxis' : 'events',
# 'fold' : 2
# }
variables['nJet']  = {   'name': 'Sum$(CleanJet_pt>30)',
                         'range' : (4,0,4),
                         'xaxis' : 'njets',
                         'fold' : 2
                         }


variables['nLepton'] =  {
    'name': '1*(Alt$(Lepton_pt[0],0.)>10) + 1*(Alt$(Lepton_pt[1],0.)>10) + 1*(Alt$(Lepton_pt[2],0.)>10)+ 1*(Alt$(Lepton_pt[3],0.)>10) + 1*(Alt$(Lepton_pt[4],0.)>10)',
    'range': (5,0,5),
    'xaxis': '# leptons',
    'fold': 2
}
variables['mll']  = {   'name': 'mll',            #   variable name
                        'range' : (4, 0. ,500),    #   variable range
                        'xaxis' : 'mll [GeV]',  #   x axis name
                        'fold' : 2
                        }
variables['mll_v3']  = {   'name': 'mll',            #   variable name
                           'range' : (12, 20. ,320),    #   variable range
                           'xaxis' : 'mll [GeV]',  #   x axis name
                           'fold' : 2
                           }
variables['mll_v2']  = {   'name': 'mll',            #   variable name
                           'range' : (80, 0. ,800),    #   variable range
                           'xaxis' : 'mll [GeV]',  #   x axis name
                           'fold' : 2
                           }
variables['mjj']  = {  'name': 'mjj',
                       'range': ([500,800,1100,1500,2000],),  #for 500 < mjj < 1000
                       'xaxis': 'mjj [GeV]',
                       'fold': 2
                       }
variables['mjj_fold3']  = {  'name': 'mjj',
                       'range': ([500,800,1100,1500,2000],),  #for 500 < mjj < 1000
                       'xaxis': 'mjj [GeV]',
                       'fold': 3
                       }
variables['mjj_v2']  = {  'name': 'mjj',
                          'range': (10,150,500),  #for 500 < mjj < 1000
                          'xaxis': 'mjj [GeV]',
                          'fold': 2
                          }

variables['mjj_v3']  = {  'name': 'mjj',
                          'range': (20, 0. ,2000),  #for 500 < mjj < 1000
                          'xaxis': 'mjj [GeV]',
                          'fold': 2
                          }
variables['pt1']  = {   'name': 'Alt$(Lepton_pt[0],-9999.)',
                        'range' : (10,30.,300),
                        'xaxis' : 'p_{T} 1st lep',
                        'fold'  : 2
                        }
variables['pt1_v2']  = {   'name': 'Alt$(Lepton_pt[0],-9999.)',
                           'range' : (12,30.,300),
                           'xaxis' : 'p_{T} 1st lep',
                           'fold'  : 2
                           }

variables['pt2']  = {   'name': 'Alt$(Lepton_pt[1],-9999.)',
                        'range' : (10,30.,180),
                        'xaxis' : 'p_{T} 2nd lep',
                        'fold'  : 2
                        }
variables['pt2_v2']  = {   'name': 'Alt$(Lepton_pt[1],-9999.)',
                           'range' : (10,30.,150),
                           'xaxis' : 'p_{T} 2nd lep',
                           'fold'  : 2
                           }

variables['jetpt1']  = {   'name': 'Alt$(CleanJet_pt[0],-9999.)',
                           'range' : (10,30.,350),
                           'xaxis' : 'p_{T} 1st jet',
                           'fold'  : 2
                           }

variables['jetpt2']  = {   'name': 'Alt$(CleanJet_pt[1],-9999.)',
                           'range' : (10,30.,350),
                           'xaxis' : 'p_{T} 2nd jet',
                           'fold'  : 2
                           }

variables['met']  = {   'name': 'MET_pt',            #   variable name
                        'range' : (10,0,200),    #   variable range
                        'xaxis' : 'pfmet [GeV]',  #   x axis name
                        'fold' : 2
                        }

variables['etaj1'] = {  'name': 'Alt$(CleanJet_eta[0],-9999.)',
                        'range': (10,-5,5),
                        'xaxis': 'etaj1',
                        'fold': 2
                        }

variables['etaj2'] = {         'name': 'Alt$(CleanJet_eta[1],-9999.)',
                               'range': (10,-5,5),
                               'xaxis': 'etaj2',
                               'fold': 2
                               }

variables['detajj']  = {  'name': 'detajj',
                          'range': (7,0.0,7.0),

                          'xaxis': 'detajj',
                          'fold': 2
                          }

variables['Zlep1']  = {  'name': '(Alt$(Lepton_eta[0],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj',
                         'range': (10,-1.,1.),
                         'xaxis': 'Z^{lep}_{1}',
                         'fold': 2
                         }

variables['Zlep2']  = {  'name': '(Alt$(Lepton_eta[1],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj',
                         'range': (10,-1.,1.),
                         'xaxis': 'Z^{lep}_{2}',
                         'fold': 2
                         }
