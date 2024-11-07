dates <- as.factor(demo[1, -1])
variety <- as.factor(demo[5, -1])
times <- as.factor(demo[2, -1])

plot(dat[,1], dat[,2], type = "n", 
     ylab = "Reflectance", xlab = "Wavelength")
for(k in 2:ncol(dat))
{
  lines(dat[,1], dat[,k], col = dates[k-1])
}
legend("topleft", col = c(1,2), legend = levels(dates), lty = 1)
