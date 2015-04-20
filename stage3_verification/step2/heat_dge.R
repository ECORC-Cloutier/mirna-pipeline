#Control_Vs_Heat
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
file_heat = heat_file #input file
data_heat <- read.delim(file_heat, header=TRUE, sep=',')
data2_heat <- data_heat[,2:7]
rownames(data2_heat) <- data_heat[,1]
group_heat <- c(rep("Control",3),rep("Heat",3))

#cpm
cpm_heat = cpm(data2_heat)
write.table(cpm_heat, file = "CPM_Control_Vs_Heat.csv", quote=FALSE, sep=",", col.names = NA)

#DGEList
data2_heat <- DGEList(counts=data2_heat, group=group_heat)
data2_heat$samples

plotMDS(data2_heat)

#saving MDS graph
dev.copy(png,'Control_Vs_heat_MDS.png')
dev.off()

data2_heat <- estimateCommonDisp(data2_heat)
data2_heat <- estimateTagwiseDisp(data2_heat, prior.df = 20)
#data2_heat <- estimateTagwiseDisp(data2_heat)

#plotMeanVar and plotBCV
plotMeanVar(data2_heat, show.tagwise.vars = TRUE, NBline = TRUE)
dev.copy(png,'Control_Vs_heat_MeanVar.png')
dev.off()

plotBCV(data2_heat)
dev.copy(png,'Control_Vs_heat_BCV.png')
dev.off()

de_Ctrl_heat <- exactTest (data2_heat, pair=c("Control","Heat"))

#top 10 tags
#top_tags = topTags(de_Ctrl_heat, n=36, adjust.method="none")
top_tags = topTags(de_Ctrl_heat,n=36)
raise2_values = 2^(top_tags$table[,1])
top_tags = cbind(top_tags$table, Actual_fold_change = raise2_values)
# print (top_tags)
#top_tags.table <- top_tags$table
#write.table(top_tags.table, file = "DE_day10_Control_Vs_Heat_top_10_tags.csv", sep=",", col.names = NA)

#sh = summary(de_Ctrl_heat_fdr <- decideTestsDGE(de_Ctrl_heat, p=0.1))
#sh = summary(de_Ctrl_heat_fdr <- decideTestsDGE(de_Ctrl_heat, p=0.05))
sh = summary(de_Ctrl_heat_fdr <- decideTestsDGE(de_Ctrl_heat, adjust.method = "none", p=0.1))
print (sh)

de_ctrl_heat.table <- de_Ctrl_heat$table
write.table(de_ctrl_heat.table, file = "DE_Control_Vs_Heat.csv", quote=FALSE, sep=",", col.names = NA)

#PValue <= 0.1
filtered_heat_d10  <- subset(top_tags, top_tags$PValue <= 0.1)
filtered_heat_d10 <- filtered_heat_d10[order(-filtered_heat_d10$logFC),] 
write.table(filtered_heat_d10, file = "DE_Control_Vs_Heat_filtered.csv", quote=FALSE, sep=",", col.names = NA)

detags <- rownames(data2_heat)[as.logical(de_Ctrl_heat_fdr)]
plotSmear(de_Ctrl_heat, de.tags=detags)

#saving logFC_Vs_logCPM graph
dev.copy(png,'Control_Vs_heat_logFC_Vs_logCPM.png')
dev.off()