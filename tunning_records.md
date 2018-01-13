# 2018-1-11-17-54
- 3min 8 epoches
- ok while driving(maybe accidental)
- val_loss:0.014
# 2018-1-11-18-28
- add random_fliplr
- 3.8min 8 epoches
- val_loss best at 7th epoch
- val_loss:0.0116
- failed while driving
# 2018-1-11-18-42
- same as 2018-1-11-17-54
- del random_fliplr
- failed while driving
- failed after off line
# 2018-1-11-18-58
- add random_shear
- overfitting (how much is the diff of two loss)
- 5.2min 8 epoches
- val_loss:0.0206
- failed while driving
# 2018-1-11-19-51
- val_loss: 0.02847931762519443
- time consume:63.39696011940638 min 8 epoches
- failed while driving
- rotate spend too much time? yes
# 2018-1-11-21-23
- val_loss: 0.037187330104296416
- time consume:7.752584358056386 min 8 epoches
- overfitting
- failed while driving
# 2018-1-11-21-36
- val_loss: 0.01956899816033889
- time consume:7.666866683959961 min 8 epoches
- modify resize shape to (64, 64)
- almost no effect in time consuming
- overfitting is best among these
- failed while driving
# 2018-1-11-21-52
- val_loss: 0.013784210083393771
- time consume:3.4825925628344216 min 8 epoches
- del all data augment
- failed while driving
- stick on the road side
# 2018-1-11-22-8
- val_loss: 0.013592196735148866
- time consume:7.627757140000662 min 8 epoches
- add 3 MaxPooling2D, and valid2same
- overfitting is small
- failed while driving
# 2018-1-11-22-23
- val_loss: 0.012203519416614428
- time consume:7.77211906115214 min 8 epoches
- add another two MaxPooling2D and valid2same
- ok but not good while driving
# 2018-1-11-22-52
- val_loss: 0.018610978289626323
- time consume:7.7907503843307495 min 8 epoches
- decrease lr to 0.0001
- maybe need more epoches?
# 2018-1-11-23-4
- val_loss: 0.014858048950247404
- time consume:11.802288389205932 min 12 epoches
- ok but not good can back off the road
- see the model_loss val_loss is lower than train_loss
# 2018-1-11-23-25
- val_loss: 0.012955437223958501
- time consume:7.825041651725769 min 8 epoches
# 2018-1-11-23-45
- val_loss: 0.011735256672463994
- time consume:7.9196258624394735 min 8 epoches
- add three dropout
- knock down the tree
# 2018-1-12-0-0
- val_loss: 0.04415837699449042
- time consume:7.75702608426412 min 8 epoches
# 2018-1-12-0-12
- val_loss: 0.06262126228624552
- time consume:7.659123925367991 min 8 epoches
# 2018-1-12-0-21
- val_loss: 0.010559555052187027
- time consume:7.638488181432089 min 8 epoches
- although loss is very small and overfitting is good, but failed while driving.
- so dropout is not useful for this Project
# 2018-1-12-0-33
- val_loss: 0.014124023964473093
- time consume:7.646923661231995 min 8 epoches
# 2018-1-12-0-58
- val_loss: 0.013416333277694103
- time consume:7.669753249486288 min 8 epoches
# 2018-1-12-1-9
- val_loss: 0.012689829797731707
- time consume:7.97845413684845 min 8 epoches
# 2018-1-12-1-23
- val_loss: 0.013350695625624874
- time consume:7.96855195760727 min 8 epoches
- data balance: modeify image_random_read
- ok if speed fixed at 10,but will step the line.
# 2018-1-12-1-58
- val_loss: 0.012880022051157776
- time consume:8.017259526252747 min 8 epoches
- almost ok at speed 30
- tune the param of image_random_read
# 2018-1-12-2-15
- val_loss: 0.01982619272741048
- time consume:7.935977085431417 min 8 epoches
# 2018-1-12-14-24
- val_loss: 0.0029222947042925576
- time consume:6.666314375400543 min 8 epoches
# 2018-1-12-16-25
- val_loss: 0.0034730010757859993
- time consume:7.07138751745224 min 8 epoches
# 2018-1-12-17-2
- val_loss: 4.726900405596792e-08
- time consume:3.212162530422211 min 8 epoches
# 2018-1-12-17-9
- val_loss: 3.2399094188325476e-06
- time consume:0.8268154780069987 min 2 epoches
# 2018-1-12-17-13
- val_loss: 3.086169338217815e-07
- time consume:0.9056920091311137 min 2 epoches
# 2018-1-12-17-22
- val_loss: 2.886537401991518e-06
- time consume:0.876044241587321 min 2 epoches
# 2018-1-12-17-28
- val_loss: 0.010375041090883315
- time consume:0.8947980483373006 min 2 epoches
# 2018-1-12-17-37
- val_loss: 0.014315756843425334
- time consume:0.9083797852198283 min 2 epoches
# 2018-1-12-17-44
- val_loss: 0.01892525452728334
- time consume:4.4037972013155615 min 5 epoches
# 2018-1-12-17-55
- val_loss: 0.008550868908825674
- time consume:2.158025888601939 min 5 epoches
# 2018-1-12-18-1
- val_loss: 0.006645338278950045
- time consume:2.037530533472697 min 5 epoches
# 2018-1-12-18-9
- val_loss: 0.009515004514373447
- time consume:0.8316865960756937 min 2 epoches
# 2018-1-12-18-13
- val_loss: 0.01013258914463222
- time consume:0.8139395435651143 min 2 epoches
# 2018-1-12-18-23
- val_loss: 0.009626619027633416
- time consume:0.8196441451708476 min 2 epoches
# 2018-1-12-18-35
- val_loss: 0.010150367283801498
- time consume:0.8131075898806254 min 2 epoches
# 2018-1-12-18-42
- val_loss: 0.010582858279935624
- time consume:0.8774341185887654 min 2 epoches
# 2018-1-12-18-47
- val_loss: 0.010156265705039627
- time consume:0.8731288472811382 min 2 epoches
# 2018-1-12-18-52
- val_loss: 0.009662754760172806
- time consume:0.8897141059239705 min 2 epoches
# 2018-1-12-18-58
- val_loss: 0.010596297264687325
- time consume:0.8790909488995869 min 2 epoches
# 2018-1-12-19-13
- val_loss: 0.009609191690718657
- time consume:0.823069695631663 min 2 epoches
# 2018-1-12-19-18
- val_loss: 0.00907390822019232
- time consume:0.8076470295588175 min 2 epoches
# 2018-1-12-19-21
- val_loss: 0.011210752173179859
- time consume:0.799559477965037 min 2 epoches
# 2018-1-12-19-29
- val_loss: 0.010938391971744989
- time consume:0.7928000211715698 min 2 epoches
# 2018-1-12-19-35
- val_loss: 0.011246623299819859
- time consume:0.9163323481877644 min 2 epoches
# 2018-1-12-19-40
- val_loss: 0.008657593231060003
- time consume:0.8117687622706096 min 2 epoches
# 2018-1-12-21-38
- val_loss: 0.009369776461665568
- time consume:0.8914376298586527 min 2 epoches
- find the diff between cv2.imread and plt.imread
# 2018-1-12-21-40
- val_loss: 0.012279924838558623
- time consume:1.0014304478963216 min 2 epoches
# 2018-1-12-21-45
- val_loss: 0.033178557935906086
- time consume:1.8867113828659057 min 2 epoches
# 2018-1-12-21-57
- val_loss: 0.021741772597459585
- time consume:0.8634533564249675 min 2 epoches
# 2018-1-12-22-6
- val_loss: 0.014224617171292553
- time consume:5.125785291194916 min 5 epoches
# 2018-1-12-22-33
- val_loss: 0.01836176103401164
- time consume:1.8841767271359762 min 2 epoches
- add dropout
# 2018-1-12-22-42
- val_loss: 0.011118591336614957
- time consume:4.547065281867981 min 5 epoches
