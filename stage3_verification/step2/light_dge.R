#Control_Vs_light
#Original Author: Md Safiur Rahman Mahdi
#Modified: April 16, 2015 by Douglas Huang
#Function: Performs differential gene expression analysis on heat stress
#Instructions: Use the directory path and filename as command-line arguments

library(edgeR)

#get filename from command line
args <- commandArgs(trailingOnly = TRUE)
print(args)
workdir <- args[1]
heat_file <- args[2]
rm(args)

setwd(workdir) # enter directory here 

#creating matrix
file_light = "day_10_Control_Vs_Light_grouped_family.csv" #input file
data_light <- read.delim(file_light, header=TRUE, sep=',')
data2_light <- data_light[,2:7]
rownames(data2_light) <- data_light[,1]
group_l0 <- c(rep("Control",3),rep("light",3))

#cpm
cpm_light = cpm(data2_light)
write.table(cpm_light, file = "CPM_Control_Vs_Light.csv", quote=FALSE, sep=",", col.names = NA)

data2_light <- DGEList(counts=data2_light, group=group_l0)
data2_light$samples

plotMDS(data2_light)
#saving MDS graph
dev.copy(png,'Control_Vs_light_MDS.png')
dev.off()

data2_light <- estimateCommonDisp(data2_light)
data2_light <- estimateTagwiseDisp(data2_light, prior.df = 20)
#data2_light <- estimateTagwiseDisp(data2_light)

#plotMeanVar and plotBCV
plotMeanVar(data2_light, show.tagwise.vars = TRUE, NBline = TRUE)
dev.copy(png,'Control_Vs_light_MeanVar.png')
dev.off()

plotBCV(data2_light)
dev.copy(png,'Control_Vs_light_BCV.png')
dev.off()

de_Ctrl_light <- exactTest (data2_light, pair=c("Control","light"))

#top 10 tags
#top_tags = topTags(de_Ctrl_heat, n=36, adjust.method="none")
top_tags = topTags(de_Ctrl_light,n=36)
raise2_values = 2^(top_tags$table[,1]) 
top_tags = cbind(top_tags$table, Actual_fold_change = raise2_values)
# print (top_tags)

#sl = summary(de_Ctrl_light_fdr <- decideTestsDGE(de_Ctrl_light, p=0.1))
#sl = summary(de_Ctrl_light_fdr <- decideTestsDGE(de_Ctrl_light, p=0.05))
sl = summary(de_Ctrl_light_fdr <- decideTestsDGE(de_Ctrl_light, adjust.method="none", p=0.1))
print (sl)

de_ctrl_light.table <- de_Ctrl_light$table
write.table(de_ctrl_light.table, file = "DE_Control_Vs_light.csv", quote=FALSE, sep=",", col.names = NA)

#PValue <= 0.1
filtered_light_d10  <- subset(top_tags, top_tags$PValue <= 0.1)
filtered_light_d10 <- filtered_light_d10[order(-filtered_light_d10$logFC),] 
write.table(filtered_light_d10, file = "DE_Control_Vs_Light_filtered.csv", quote=FALSE, sep=",", col.names = NA)

detags <- rownames(data2_light)[as.logical(de_Ctrl_light_fdr)]
plotSmear(de_Ctrl_light, de.tags=detags)

#saving logFC_Vs_logCPM graph
dev.copy(png,'Control_Vs_light_logFC_Vs_logCPM.png')
dev.off()