
sub L_RULE_WRITE{

	&CHARA_MAIN_OPEN;
	&TIME_DATA;
	&HOST_NAME;
	&COUNTRY_DATA_OPEN("$kcon");

	if($xcid eq "0"){&ERR("����λ�� ������ �� �����ϴ�.");}
	if(length($in{'title'}) > 40 || length($in{'ins'}) > 500) { &ERR("�� �� �����ϰ� ������ ���� �ֽʽÿ�."); }
	if($in{'ins'} eq "") { &ERR("�޼����� �ԷµǾ� ���� �ʽ��ϴ�."); }

	open(IN,"$LOCAL_LIST") or &ERR2('������ ���� �ʾҽ��ϴ�. err no :country');
	@LOCAL_DATA = <IN>;
	close(IN);

	$bbs_num = @LOCAL_DATA;
	if($bbs_num > $MES_MAX) { pop(@LOCAL_DATA); }

	($bbid,$bbno)=split(/<>/,$LOCAL_DATA[0]);
	$s_no=$bbno+1;

	$numm = int($cex / $LANK);
	if($numm>20){$numm = 20;}
	$bbname = "$kname";
	if($in{"type"} eq "all"){$bbtype = 1;}else{$bbtype = 0;}
	unshift(@LOCAL_DATA,"$kid<>$s_no<>$in{'ins'}<>$kchara<>$bbname<>$host<>$daytime<>$kele<>$kcon<>$bbtype<>\n");

	open(OUT,">$LOCAL_LIST") or &ERR('������ ���� �ʾҽ��ϴ�.');
	print OUT @LOCAL_DATA;
	close(OUT);

	&HEADER;
	print <<"EOM";
<CENTER><hr size=0><h2>������ �����߽��ϴ�.</h2><p>

<form action="$FILE_MYDATA" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=LOCAL_RULE>
<input type=submit value="Ȯ��"></form></CENTER>
EOM
	&FOOTER;
	exit;
	
}
1;