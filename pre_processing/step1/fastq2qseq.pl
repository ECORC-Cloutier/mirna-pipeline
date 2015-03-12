#!/opt/perl-5.8.8/bin/perl 
#############################################################################
#
#                            PUBLIC DOMAIN NOTICE
#               National Center for Biotechnology Information
#
#  This software/database is a "United States Government Work" under the
#  terms of the United States Copyright Act.  It was written as part of
#  the author's official duties as a United States Government employee and
#  thus cannot be copyrighted.  This software/database is freely available
#  to the public for use. The National Library of Medicine and the U.S.
#  Government have not placed any restriction on its use or reproduction.
#
#  Although all reasonable efforts have been taken to ensure the accuracy
#  and reliability of the software and data, the NLM and the U.S.
#  Government do not and cannot warrant the performance or results that
#  may be obtained by using this software or data. The NLM and the U.S.
#  Government disclaim all warranties, express or implied, including
#  warranties of performance, merchantability or fitness for any particular
#  purpose.
#
#  Please cite the author in any work or product based on this material.
#
############################################################################
use strict;

if ( ( scalar @ARGV ) eq 0 && ( -t STDIN ) )
    {
        die "'fastq2qseq.pl < fastq file >' OR '| fastq2qseq.pl'\n";
    }


while (<>)
    {
        s/^@//; chomp;
        my $Seq = <>; chomp $Seq;
        <>;
        my $Qual = <>; chomp $Qual;


        my ($Read,$Barcode,$Y,$X,$Tile,$Lane,$Run);


        if ( m/\/(\d{1})$/ )
            {
                $Read = $1; s/\/\d{1}$//;
            }
        if ( m/\#(\S+)$/ )
            {
                $Barcode = $1; s/#\S+$//;
            }
        if ( m/[:_](\d+)$/ )
            {
                $Y = $1; s/[:_]\d+$//;
            }
        if ( m/[:_](\d+)$/ )
            {
                $X = $1; s/[:_]\d+$//;
            }
        if ( m/[:_](\d+)$/ )
            {
                $Tile = $1; s/[:_]\d+$//;
            }
        if ( m/[:_](\d+)$/ )
            {
                $Lane = $1; s/[:_]\d+$//;
            }
        if ( m/[:_](\d+)$/ )
            {
                $Run = $1; s/[:_]\d+$//;
            }


        print "$_\t$Run\t$Lane\t$Tile\t$X\t$Y\t$Barcode\t$Read\t$Seq\t$Qual\t1\n";
    }
