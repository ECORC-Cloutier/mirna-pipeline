#Control_Vs_UV
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
file_uv = "day_10_Control_Vs_UV_grouped_family.csv" #input file
data_uv0 <- read.delim(file_uv, header=TRUE, sep=',')
data2_uv <- data_uv0[,2:7]
rownames(data2_uv) <- data_uv0[,1]
group_uv0 <- c(rep("Control",3),rep("uv",3))

#cpm
cpm_uv = cpm(data2_uv)
write.table(cpm_uv, file = "CPM_Control_Vs_UV.csv", quote=FALSE, sep=",", col.names = NA)

data2_uv <- DGEList(counts=data2_uv, group=group_uv0)
data2_uv$samples

plotMDS(data2_uv)
#saving MDS graph
dev.copy(png,'Control_Vs_uv_MDS.png')
dev.off()

data2_uv <- estimateCommonDisp(data2_uv)
data2_uv <- estimateTagwiseDisp(data2_uv, prior.df = 20)
#data2_uv <- estimateTagwiseDisp(data2_uv)

#plotMeanVar and plotBCV
plotMeanVar(data2_uv, show.tagwise.vars = TRUE, NBline = TRUE)
dev.copy(png,'Control_Vs_UV_MeanVar.png')
dev.off()

plotBCV(data2_uv)
dev.copy(png,'Control_Vs_UV_BCV.png')
dev.off()

de_Ctrl_uv <- exactTest (data2_uv, pair=c("Control","uv"))

#top 10 tags
#top_tags = topTags(de_Ctrl_heat, n=36, adjust.method="none")
top_tags = topTags(de_Ctrl_uv,n=36)
raise2_values = 2^(top_tags$table[,1])
top_tags = cbind(top_tags$table, Actual_fold_change = raise2_values)
# print (top_tags)

#suv = summary(de_Ctrl_uv_fdr <- decideTestsDGE(de_Ctrl_uv, p=0.1))
#suv = summary(de_Ctrl_uv_fdr <- decideTestsDGE(de_Ctrl_uv, p=0.05))
suv = summary(de_Ctrl_uv_fdr <- decideTestsDGE(de_Ctrl_uv, adjust.method="none", p=0.1))
print (suv)

de_ctrl_uv.table <- de_Ctrl_uv$table
write.table(de_ctrl_uv.table, file = "DE_Control_Vs_uv.csv", quote=FALSE, sep=",", col.names = NA)

#PValue <= 0.1
filtered_uv_d10  <- subset(top_tags, top_tags$PValue <= 0.1)
filtered_uv_d10 <- filtered_uv_d10[order(-filtered_uv_d10$logFC),] 
write.table(filtered_uv_d10, file = "DE_Control_Vs_uv_filtered.csv", quote=FALSE, sep=",", col.names = NA)

detags <- rownames(data2_uv)[as.logical(de_Ctrl_uv_fdr)]
plotSmear(de_Ctrl_uv, de.tags=detags)

#saving logFC_Vs_logCPM graph
dev.copy(png,'Control_Vs_uv_logFC_Vs_logCPM.png')
dev.off()