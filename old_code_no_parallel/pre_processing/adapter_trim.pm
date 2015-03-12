package adapter_trim;
require Exporter;
use String::Approx 'amatch';

#fuzzy matching for 3' adapter trimming off of Illumina and SOLiD small RNA reads

our @ISA = qw(Exporter);
our @EXPORT = qw(find_adaptor);

my $MAX_ADAPTER = 15; #largest amount of adapter to look at, providing more than this many bases to $opt_a won't be used
my $MAX_ADAPTER_MISMATCH = 2; #max mismatches allowed for fuzzy matching
my $MID_ADAPTER = 8; #between this and $MAX_ADAPTER bp of adapter sequence, look only at the end with a different MISMATCH threshold
my $MID_ADAPTER_MISMATCH = 1; #max mismatches allowed for fuzzy matching from $MID_ADAPTER to $MAX_ADAPTER -1

sub find_adaptor {
	my $read = shift;
	my $vector = shift;
	my $read_length = shift;

	#first, take the first $MAX_ADAPTER bp of the adapter and see if it matches the head of the read, which indicates an adapter dimer
	#the first 2 or 3 bases of the adapter can be merged into the index in an adapter dimer, so check the front of the read for the first few $MAX_ADAPTERmer windows of the adapter
	for (my $i = 0; $i < 4; $i++) {
		return 0 if amatch(substr($vector, $i, $MAX_ADAPTER), ["S$MAX_ADAPTER_MISMATCH", "I0", "D0", "initial_position=0", "final_position=$MAX_ADAPTER"], $read);
	}
	
	#check anywhere along the length of the read for $MAX_ADAPTER, try for an exact match first to save time
	my $max_adapter = substr($vector, 0, $MAX_ADAPTER);
	my $index_pos = index($read, $max_adapter);
	return $index_pos if $index_pos > 0;
	#now read backwards from the end of the read using fuzzy matching
	for (my $i = $read_length - $MAX_ADAPTER; $i > 0; $i--) {
		return $i if amatch(substr($vector, 0, $MAX_ADAPTER), ["S$MAX_ADAPTER_MISMATCH", "I0", "D0", "initial_position=$i"], $read);
	}

	#check for decreasing bases of adapter from the end using fuzzy matching constraints
	for (my $v = $MAX_ADAPTER; $v > $MID_ADAPTER; $v--) {
		my $init_pos = $read_length - $v;
		return $init_pos if amatch(substr($vector, 0, $v), ["S$MID_ADAPTER_MISMATCH", "I0", "D0", "initial_position=$init_pos"], $read);
	}

	#check from the end for an exact match for small pieces of vector
	for (my $i = $MID_ADAPTER; $i > 0; $i--) {
		my $init_pos = $read_length - $i;
		return $init_pos if substr($vector, 0, $i) eq substr($read, $init_pos);
	}

	return -1;
}

1;
