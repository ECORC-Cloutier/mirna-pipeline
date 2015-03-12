fastq_qseq()
{
    file=$1
    base=${file%%.*}
    perl fastq2qseq.pl < $file > ${base}.txt
}

trim()
{
    file=$1
    sequence=$2
    base=${file%%.*}
    perl adapter_trim.pl -a $sequence -r ${base}_report.txt < $file > ${base}_trimmed.txt  #adapter sequence at -a
}

qseq_fastq()
{
    file=$1
    base=${file%%.*}
    perl qseq2fastq.pl < $file > ${base}.fastq
}

aggregate_fasta() 
{
    src=$1
    base=${src%%.*}
    mkdir ${base}
	cp $src ${base}/master.fasta
	cp aggregate_whole_no_wg.py ${base}
	cd ${base}
	python aggregate_whole_no_wg.py
	cd ..
	mv $src save_fasta
}

replicate_split()
{
    next=$1
    cp splitFasta.py ${next}
    cd ${next}
    python splitFasta.py 300 ${next}_uniq.fasta
    cd ..
}

launch_cat()
{
    src=$1
    cp CAT1.* newFilter.py run_filter_cat.sh ${src}	
    filename=${src}_uniq.fasta
    cd ${src}
    bash run_filter_cat.sh $filename
    cd ..
}

launch_gene()
{
    src=$1
    cp GENE.* newFilter.py run_filter_gene.sh ${src}	
    filename=${src}_uniq.fasta
    cd ${src}
    bash run_filter_gene.sh $filename
    cd ..
}

launch_lncrna()
{
    src=$1
    cp LNCRNA.* newFilter.py run_filter_lncrna.sh ${src}	
    filename=${src}_uniq.fasta
    cd ${src}
    bash run_filter_lncrna.sh $filename
    cd ..
}

launch_chloro()
{
    src=$1
    cp CHLORO.* newFilter.py run_filter_chloro.sh ${src}	
    filename=${src}_uniq.fasta
    cd ${src}
    bash run_filter_chloro.sh $filename
    cd ..
}

replicate_crush()
{
    next=$1
    cp crush.py ${next}
	cd ${next}
	python crush.py ${next}_summary.csv ${next}_uniq.fasta.ncglch
    cd ..
}

master_fasta()
{
    file=$1
    python make_master.py $file
}

find_mature()
{
    file=$1
    base=${file%%.*}
    mkdir ${base}
    cp find_mature_0mm.py MPC* $file $base
    cd $base
    python find_mature_0mm.py $file MPC $file MPC.fa
    cd ..
}

find_mature_novel()
{
    file=$1
    cp find_mature_1_4mm.py $file
    cd $file
    name=${file}.fasta_1_4mm.fa
    python find_mature_1_4mm.py $name MPC $name MPC.fa
    cd ..
}

create_rpm_0mm()
{
    file=$1
    base=${file%%.*}
    mkdir $base
    cp create_id_rpmlist.py $base
    file1=${base}.smaller.cons
    file2=${base}_cons_master.fasta_mature.csv
    file3=${base}_cons_master.fasta_1_4mm.fa_mature.csv
    mv $file $file1 $file2 $file3 $base
    cd $base
    python create_id_rpmlist.py $file1 $file2 0 
    cd ..
}

create_rpm_1_4mm()
{
    file=$1    
    cd $file
    file1=${file}.smaller.cons
    file2=${file}_cons_master.fasta_1_4mm.fa_mature.csv
    python create_id_rpmlist.py $file1 $file2 1_4 
    cd ..
}

align_group()
{
    file=$1
    base=${file%%.fa}
    mkdir $base
    mv $file $base
    cp msa.py extract_precursor.py trit* hairpin.fa $base
    cd $base
    python msa.py $file $OLDPWD/Triticum_aestivum_UK454_LCGAssembly.fa
    cd ..
}

