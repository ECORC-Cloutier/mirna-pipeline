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

my ( $MACH, $RUN, $LANE, $TILE, $X, $Y, $BARCODE, $READ, $SEQ, $QUAL, $FILTER )
    = ( 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 );
my $sep = ':';


if ( ( scalar @ARGV ) eq 0 )
    {
        if ( -t STDIN )
            {
                print "qseq2fastq.pl <qseq file> <separator (opt, def=:)>\n";
                print "\tor\n| qseq2fastq.pl\n";
            }
        else
            {
                while (<>) { convertQseqLine ( $_ ); }
            }
    }
else
    {
        my $qseqFile = shift;
        if ( ( scalar @ARGV ) > 0 ) { $sep = shift; }
        open (QSEQ,$qseqFile) or die "Unable to open $qseqFile\n";
        while(<QSEQ>) { convertQseqLine ( $_ ); }
    }


sub convertQseqLine {
    my $line = shift;
    chomp $line;
    my $defline = "";
    my @tmp = split(/\t/,$line);
    if ( $tmp[$MACH] ne "" )
        {
            $defline .= "$tmp[$MACH]";
        }
    if ( $tmp[$RUN] ne "" )
        {
            $defline .= "$sep$tmp[$RUN]";
        }
    $defline .= "$sep$tmp[$LANE]$sep$tmp[$TILE]$sep$tmp[$X]$sep$tmp[$Y]";
    if ( $tmp[$BARCODE] ne "" )
        {
            $defline .= "#$tmp[$BARCODE]";
        }
    if ( $tmp[$READ] ne "" )
        {
            $defline .= "/$tmp[$READ]";
        }
    print "\@$defline\n$tmp[$SEQ]\n+\n$tmp[$QUAL]\n";
}

