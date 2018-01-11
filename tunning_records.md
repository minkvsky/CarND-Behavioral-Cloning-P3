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
