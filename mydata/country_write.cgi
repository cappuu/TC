sub COUNTRY_WRITE{

	&CHARA_MAIN_OPEN;
	&TIME_DATA;
	&HOST_NAME;
	&COUNTRY_DATA_OPEN("$kcon");
	&TOWN_DATA_OPEN("$kpos");

	if($xcid eq "0"){&ERR("����λ�� ������ �� �����ϴ�.");}
	if(length($in{'title'}) > 40 || length($in{'ins'}) > 1000) { &ERR("�� �� �����ϰ� ���� ���ּ���"); }

	if(($in{'title'} eq "" && $in{'b_no'} eq "")|| $in{'ins'} eq "") { &ERR("�޼����� �Էµ����� �ʽ��ϴ�"); }

	if($lockkey) { &F_LOCK; }
	open(IN,"$BBS_LIST") or &ERR2('������ ���� �ʾҽ��ϴ�. err no :country');
	@BBS_DATA1 = <IN>;
	close(IN);

	&GWAN1;

	$bbs_num = @BBS_DATA1;
	if($bbs_num > $MES_MAX) { pop(@BBS_DATA1); }

	$bbname = "<B><font size=2><a href=\"javascript:info('$kid')\">��$kname��</a></B>ID:$kid <font size=2>����:��Lv.$klevel�� <img src=$IMG/$rank_mes\.jpg>";
	if($in{"type"} eq "all"){$bbtype = 1;$back = "COUNTRY_ALL_TALK"}else{$bbtype = 0;$back = "COUNTRY_TALK"}

	($lbbid,$lbbtitle,$lbbmes,$lbbcharaimg,$lbbname,$lbbhost,$lbbtime,$lbbele,$lbbcon,$lbbtype,$lbbno,$lbbheap)=split(/<>/,$BBS_DATA1[0]);

	$bno = $lbbno + 1;

	if($in{'b_no'} ne ""){
		$b_heap = $in{'b_no'};
	}else{
		$b_heap = 0;
	}
	$kcex += 1;
	&CHARA_MAIN_INPUT;
	unshift(@BBS_DATA1,"$kid<>$in{'title'}<>$in{'ins'}<>$kchara<>$bbname<>$host<>$daytime<>$xele<>$kcon<>$bbtype<>$bno<>$b_heap<>\n");

	

	open(OUT,">$BBS_LIST") or &ERR('������ ���� �ʾҽ��ϴ�.');
	print OUT @BBS_DATA1;
	close(OUT);

	if (-e $lockfile) { unlink($lockfile); }


	&HEADER;
	print <<"EOM";
<CENTER><hr size=0><h2>ȸ�ǽǿ� ���� �÷Ƚ��ϴ�. $zname</h2><p>

<form action="./mydata.cgi" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=$back>
<input type=submit value="Ȯ��"></form></CENTER>
EOM
	&FOOTER;
	exit;
	
}
1;