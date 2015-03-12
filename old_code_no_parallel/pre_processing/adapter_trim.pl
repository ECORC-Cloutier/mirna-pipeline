#!/usr/bin/env perl

use strict;
use Getopt::Std;
use Pod::Usage;
use File::Basename;
use lib dirname(__FILE__);
use adapter_trim;

use vars qw($opt_a $opt_r);
getopts("a:r:");

#trim off 3' adapter sequence from qseq file
#return qseq file with read and quality strings shorted by amount of adapter trimmed

my $MIN_LEN = 15; #smallest read to allowed, 15 is the smallest mature mirna for human and mouse in miRBase 13

my $usage = "$0 -a adapter sequence";
die $usage unless $opt_a;
my $report = $opt_r || "./adapter_report.txt";

my $vector = $opt_a;
my $read_length = -1;

my %trimmed_reads; #hash to store reads already trimmed so they don't have to be processed again, hash value is the offset to substr
my %report; #hash to store number of reads with adapter at each position

open REPORT, ">$report" or die "Can't write to report file $report: $!\n";
while (my $line = <STDIN>) {
	chomp $line;
	my @fields = split(/\t/, $line);
	my $prestring = join("\t", @fields[0..7]);
	my $poststring = join("\t", @fields[10..@fields-1]);
	my ($read, $quality) = @fields[8..9];

	if ($read_length == -1) {
		#set read length based on first read in input
		$read_length = length($read);
		#set up report hash
		for (my $i = 1; $i < $read_length; $i++) {
			$report{$i} = 0;
		}
	}

	if (exists $trimmed_reads{$read}) {
		print_str($read, $quality, $trimmed_reads{$read}, $prestring, $poststring);
		next;
	}

	my $offset = find_adaptor($read, $vector, $read_length);

  if ($offset >= 0) {
		$trimmed_reads{$read} = $offset;
		print_str($read, $quality, $offset, $prestring, $poststring);
	} else {
		$trimmed_reads{$read} = $read_length;
		print_str($read, $quality, $read_length, $prestring, $poststring);
 }
}

foreach my $len (sort {$a <=> $b} keys %report) {
	print REPORT "$len $report{$len}\n";
}

close REPORT;

sub print_str {
	my $read = shift;
	my $quality = shift;
	my $offset = shift;
	my $prestring = shift;
	my $poststring = shift;

	my $read_str = substr($read, 0, $offset);
	my $qual_str = substr($quality, 0, $offset);
	
	$report{$offset}++;

	return if $offset < $MIN_LEN;

	print "$prestring\t$read_str\t$qual_str\t$poststring\n";
}
