#installing binaries from directory

pack_list <- list.files("/Users/aidenjohnson/projects/festive-squirrel/r-package-binaries/", full.names = T)
print(pack_list)
for(i in pack_list){
  install.packages(i, repos =NULL, type ="source") 
}
