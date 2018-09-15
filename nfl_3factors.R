data.fac <- read.csv("wins.csv")


data.fac$PassOff = data.fac$Wins
data.fac$PassDef = data.fac$Wins
passing <- read.csv("passing.csv",header=T)
for (i in 1:dim(data.fac)[1]){
 k = which(as.character(passing$TeamSeason) == as.character(data.fac[i,]$Team))
 data.fac[i,]$PassOff = passing[k,]$Offense
 data.fac[i,]$PassDef = passing[k,]$Defense
 }


data.fac$RushOff = data.fac$Wins
data.fac$RushDef = data.fac$Wins
rushing <- read.csv("rushing.csv",header=T)
for (i in 1:dim(data.fac)[1]){
 k = which(as.character(rushing$TeamSeason) == as.character(data.fac[i,]$Team))
 data.fac[i,]$RushOff = rushing[k,]$Offense
 data.fac[i,]$RushDef = rushing[k,]$Defense
 }

data.fac$SpecialOff = data.fac$Wins
data.fac$SpecialDef = data.fac$Wins
special <-read.csv("special.csv",header=T) 
for (i in 1:dim(data.fac)[1]){
 k = which(as.character(special$TeamSeason) == as.character(data.fac[i,]$Team))
 data.fac[i,]$SpecialOff = special[k,]$Offense
 data.fac[i,]$SpecialDef = special[k,]$Defense
 }

nfl.4factors <- lm(Wins~PassOff+PassDef+RushOff+RushDef+SpecialOff+SpecialDef,data=data.fac)

library(car)

Anova(nfl.4factors)
