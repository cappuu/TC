

sub KING_COM {

	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kcon);
	&GWAN2;
	&TOWN_DATA_OPEN("$kpos");


	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR("���� ���� ����!");
			}
			@page = <page>;
			close(page);
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);

	$i=0;
	foreach(@TOWN_DATA){
		($zxname,$zxcon,$zxnum,$zxnou,$zxsyo,$zshiro)=split(/<>/);
		if($i < 53){
		if($kcon eq $zxcon){
		$bonglist .= "<option value=$i>$zxname";
		}
		}else{}
		$i++;
	}

	foreach(@CL_DATA) {
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/);
		if(($kid ne $eid && $xking ne $eid)  && $kcon eq $econ){
			if($x0 eq $eid || $x1 eq $eid || $x2 eq $eid || $x3 eq $eid || $x4 eq $eid || $x5 eq $eid || $x6 eq $eid || $x7 eq $eid || $x8 eq $eid || $x9 eq $eid || $x10 eq $eid || $x11 eq $eid || $x12 eq $eid || $x13 eq $eid || $x14 eq $eid || $x15 eq $eid || $x16 eq $eid || $x17 eq $eid || $x18 eq $eid || $x19 eq $eid || $x20 eq $eid || $x21 eq $eid || $x22 eq $eid || $x23 eq $eid || $x24 eq $eid || $x25 eq $eid || $x26 eq $eid){
			}else{
			$list .= "<option value=$eid>$ename ����:$estr������:$eint������:$elea������:$echa��";
			}
			if($xking eq $kid || $x0 eq $kid){
			if($x0 eq $eid || $x1 eq $eid || $x2 eq $eid || $x3 eq $eid || $x4 eq $eid || $x5 eq $eid || $x6 eq $eid || $x7 eq $eid || $x8 eq $eid || $x9 eq $eid || $x10 eq $eid || $x11 eq $eid || $x12 eq $eid || $x13 eq $eid || $x14 eq $eid || $x15 eq $eid || $x16 eq $eid || $x17 eq $eid || $x18 eq $eid || $x19 eq $eid || $x20 eq $eid || $x21 eq $eid || $x22 eq $eid || $x23 eq $eid || $x24 eq $eid || $x25 eq $eid || $x26 eq $eid){
			$list2 .= "<option value=$eid>$ename ����:$estr������:$eint������:$elea������:$echa��";
			}
	}

			if($x1 eq $kid){
				if($x2 eq $eid || $x3 eq $eid || $x4 eq $eid || $x5 eq $eid || $x6 eq $eid || $x7 eq $eid || $x8 eq $eid || $x9 eq $eid || $x10 eq $eid || $x11 eq $eid || $x12 eq $eid || $x13 eq $eid || $x14 eq $eid || $x15 eq $eid || $x16 eq $eid){
				$list2 .= "<option value=$eid>$ename ����:$estr������:$eint������:$elea������:$echa��";
				}
			}

			if($x2 eq $kid){
				if($x5 eq $eid || $x6 eq $eid || $x7 eq $eid || $x8 eq $eid){
				$list2 .= "<option value=$eid>$ename ����:$estr������:$eint������:$elea������:$echa��";
				}
			}

			if($x3 eq $kid){
				if($x9 eq $eid || $x10 eq $eid || $x11 eq $eid || $x12 eq $eid){
				$list2 .= "<option value=$eid>$ename ����:$estr������:$eint������:$elea������:$echa��";
				}
			}

			if($x4 eq $kid){
				if($x13 eq $eid || $x14 eq $eid || $x15 eq $eid || $x16 eq $eid){
				$list2 .= "<option value=$eid>$ename ����:$estr������:$eint������:$elea������:$echa��";
				}
			}

			if($x17 eq $kid){
				if($x18 eq $eid || $x19 eq $eid || $x20 eq $eid || $x21 eq $eid || $x22 eq $eid || $x23 eq $eid || $x24 eq $eid || $x25 eq $eid || $x26 eq $eid){
				$list2 .= "<option value=$eid>$ename ����:$estr������:$eint������:$elea������:$echa��";
				}
			}

			if($x18 eq $kid){
				if($x21 eq $eid || $x22 eq $eid){
				$list2 .= "<option value=$eid>$ename ����:$estr������:$eint������:$elea������:$echa��";
				}
			}

			if($x19 eq $kid){
				if($x23 eq $eid || $x24 eq $eid){
				$list2 .= "<option value=$eid>$ename ����:$estr������:$eint������:$elea������:$echa��";
				}
			}

			if($x20 eq $kid){
				if($x25 eq $eid || $x26 eq $eid){
				$list2 .= "<option value=$eid>$ename ����:$estr������:$eint������:$elea������:$echa��";
				}
			}

	}
	}
	if($xking eq "$kid"){$jjang="<form action=\./mydata.cgi\ method=\post\><TR><TH>[��������]����</TH><TH>$tname[0]</TH><TD>����������. ���� ��� ������ ����<br>����5%,��ַ�5%,����5%,�ŷ�5% ���<br>���� �� 700 �߰�</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=0><input type=submit value=�Ӹ�></TH></TR></form><form action=\./mydata.cgi\ method=\post\><TR><TH>[��������]���屺</TH><TH>$tname[1]</TH><TD>����������. ǥ���屺,�ű��屺,���屺 �λ����<br>����10%,���10% ���<br>���� �� 600 �߰�</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=1><input type=submit value=�Ӹ�></TH></TR></form><form action=\./mydata.cgi\ method=\post\><TR><TH>[��������]�»�</TH><TH>$tname[17]</TH><TD>����������. �º�,�»�,�º� �λ����<br>����10%,�ŷ�10% ���<br>���� �� 600 �߰�</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=17><input type=submit value=�Ӹ�></TH></TH></TR></form>";
$color1=1; $hae=1; $hae2=1;}

	if($xking eq "$kid" || $x0 eq "$kid"  || $x1 eq $kid || $x17 eq "$kid"){
	$jjang2="<form action=\"./bong.cgi\" method=\"POST\"><TR><TH>����й�</TH><TD colspan=2>�ڱ��� ����鿡�� ���並 �й� �Ǵ� �����մϴ�.</TD><TH><select name=num>$bonglist</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=BONG><input type=submit value=\"����\"></TH></TR></form>";
	$chset="<form action=\"./mydata.cgi\" method=\"POST\"><TR><TH>����IRCä�μ���</TH><TD colspan=2>�ڱ��� IRCä�� ������ �����մϴ�.<br>(�տ� # ���� �ʿ����)</TD><TH><input type=\"text\" name=chx size=30></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM7><input type=submit value=\"����\"></TH></TR></form>";
	}
	if($x0 eq "$kid"){$hae=1; $hae2=1;}

	if($x1 eq "$kid"){$jjang="<form action=\./mydata.cgi\ method=\post\><TR><TH>[���屺����]ǥ���屺</TH><TH>$tname[2]</TH><TD>�����屺,�����屺,�����屺,�����屺 �λ����<br>����10% ���<br>���� �� 400 �߰�</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=2><input type=submit value=�Ӹ�></TH></TR></form><form action=\./mydata.cgi\ method=\post\><TR><TH>[���屺����]�ű��屺</TH><TH>$tname[3]</TH><TD>�����屺,�����屺,�����屺,�����屺 �λ����<br>����6%,��ַ�6% ���<br>���� �� 400 �߰�</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=3><input type=submit value=�Ӹ�></TH></TR></form><form action=\./mydata.cgi\ method=\post\><TR><TH>[���屺����]���屺</TH><TH>$tname[4]</TH><TD>�ȵ��屺,�ȼ��屺,�ȳ��屺,�Ⱥ��屺 �λ����<br>��ַ�10% ���<br>���� �� 400 �߰�</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=4><input type=submit value=�Ӹ�></TH></TR></form>"; $color2=1; $hae2=1;}

	if($x17 eq "$kid"){$jjang="<form action=\./mydata.cgi\ method=\post\><TR><TH>[�»�����]�º�</TH><TH>$tname[18]</TH><TD>�����,���� �λ����<br>����10% ���<br>���� �� 400 �߰�</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=18><input type=submit value=�Ӹ�></TH></TR></form><form action=\./mydata.cgi\ method=\post\><TR><TH>[�»�����]�»�</TH><TH>$tname[19]</TH><TD>�̺λ�,ȣ�λ� �λ����<br>����6%,�ŷ�6% ���<br>���� �� 400 �߰�</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=19><input type=submit value=�Ӹ�></TH></TR></form><form action=\./mydata.cgi\ method=\post\><TR><TH>[�»�����]�º�</TH><TH>$tname[20]</TH><TD>���λ�,���λ� �λ����<br>�ŷ�10% ���<br>���� �� 400 �߰�</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=20><input type=submit value=�Ӹ�></TH></TR></form>"; $color3=1; $hae=1; $hae2=1;}
	
	if($x2 eq "$kid"){$jjang="<form action=\./mydata.cgi\ method=\post\><TR><TH>[ǥ���屺����]�����屺</TH><TH>$tname[5]</TH><TD>����6% ���<br>���� �� 200 �߰�</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=5><input type=submit value=�Ӹ�></TH></TR></form>
<form action=\./mydata.cgi\ method=\"post\"><TR><TH>[ǥ���屺����]�����屺</TH><TH>$tname[6]</TH><TD>����6% ���<br>���� �� 200 �߰�</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=6><input type=submit value=�Ӹ�></TH></TR></form>
<form action=\./mydata.cgi\ method=\"post\"><TR><TH>[ǥ���屺����]�����屺</TH><TH>$tname[7]</TH><TD>����6% ���<br>���� �� 200 �߰�</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=7><input type=submit value=�Ӹ�></TH></TR></form>
<form action=\./mydata.cgi\ method=\"post\"><TR><TH>[ǥ���屺����]�����屺</TH><TH>$tname[8]</TH><TD>����6% ���<br>���� �� 200 �߰�</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=8><input type=submit value=�Ӹ�></TH></TR></form>"; $color4=1;}

	if($x3 eq "$kid"){$jjang="<form action=\./mydata.cgi\ method=\post\><TR><TH>[�ű��屺����]�����屺</TH><TH>$tname[9]</TH><TD>����3%,��ַ�3% ���<br>���� �� 200 �߰�</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=9><input type=submit value=�Ӹ�></TH></TR></form>
<form action=\./mydata.cgi\ method=\post\"><TR><TH>[�ű��屺����]�����屺</TH><TH>$tname[10]</TH><TD>����3%,��ַ�3% ���<br>���� �� 200 �߰�</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=10><input type=submit value=�Ӹ�></TH></TR></form>
<form action=\./mydata.cgi\ method=\post\"><TR><TH>[�ű��屺����]�����屺</TH><TH>$tname[11]</TH><TD>����3%,��ַ�3% ���<br>���� �� 200 �߰�</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=11><input type=submit value=�Ӹ�></TH></TR></form>
<form action=\./mydata.cgi\ method=\post\"><TR><TH>[�ű��屺����]�����屺</TH><TH>$tname[12]</TH><TD>����3%,��ַ�3% ���<br>���� �� 200 �߰�</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=12><input type=submit value=�Ӹ�></TH></TR></form>"; $color9=1;}

	if($x4 eq "$kid"){$jjang="<form action=\./mydata.cgi\ method=\post\><TR><TH>[���屺����]�ȵ��屺</TH><TH>$tname[13]</TH><TD>��ַ�6% ���<br>���� �� 200 �߰�</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=13><input type=submit value=�Ӹ�></TH></TR></form>
<form action=\./mydata.cgi\ method=\post\><TR><TH>[���屺����]�ȼ��屺</TH><TH>$tname[14]</TH><TD>��ַ�6% ���<br>���� �� 200 �߰�</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=14><input type=submit value=�Ӹ�></TH></TR></form>
<form action=\./mydata.cgi\ method=\post\><TR><TH>[���屺����]�ȳ��屺</TH><TH>$tname[15]</TH><TD>��ַ�6% ���<br>���� �� 200 �߰�</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=15><input type=submit value=�Ӹ�></TH></TR></form>
<form action=\./mydata.cgi\ method=\post\><TR><TH>[���屺����]�Ⱥ��屺</TH><TH>$tname[16]</TH><TD>��ַ�6% ���<br>���� �� 200 �߰�</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=16><input type=submit value=�Ӹ�></TH></TR></form>"; $color5=1;}

	if($x18 eq "$kid"){$jjang="<form action=\./mydata.cgi\ method=\post\><TR><TH>[�º�����]�����</TH><TH>$tname[21]</TH><TD>����6% ���<br>���� �� 200 �߰�</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=21><input type=submit value=�Ӹ�></TH></TR></form>
<form action=\./mydata.cgi\ method=\post\><TR><TH>[�º�����]����</TH><TH>$tname[22]</TH><TD>����6% ���<br>���� �� 200 �߰�</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=22><input type=submit value=�Ӹ�></TH></TR></form>"; $color6=1;}

if($x19 eq "$kid"){$jjang="<form action=\./mydata.cgi\ method=\post\><TR><TH>[�»�����]�̺λ�</TH><TH>$tname[23]</TH><TD>����3%,�ŷ�3% ���<br>���� �� 200 �߰�</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=23><input type=submit value=�Ӹ�></TH></TR></form>
<form action=\./mydata.cgi\ method=\post\><TR><TH>[�»�����]ȣ�λ�</TH><TH>$tname[24]</TH><TD>����3%,�ŷ�3% ���<br>���� �� 200 �߰�</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=24><input type=submit value=�Ӹ�></TH></TR></form>"; $color7=1;}

if($x20 eq "$kid"){$jjang="<form action=\./mydata.cgi\ method=\post\><TR><TH>[�º�����]���λ�</TH><TH>$tname[25]</TH><TD>�ŷ�6% ���<br>���� �� 200 �߰�</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=25><input type=submit value=�Ӹ�></TH></TR></form>
<form action=\./mydata.cgi\ method=\post\><TR><TH>[�º�����]���λ�</TH><TH>$tname[26]</TH><TD>�ŷ�6% ���<br>���� �� 200 �߰�</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=26><input type=submit value=�Ӹ�></TH></TR></form>"; $color8=1;}

if($color1){$color11="bordercolor=red";}
if($color2){$color22="bordercolor=red";}
if($color3){$color33="bordercolor=red";}
if($color4){$color44="bordercolor=red";}
if($color5){$color55="bordercolor=red";}
if($color6){$color66="bordercolor=red";}
if($color7){$color77="bordercolor=red";}
if($color8){$color88="bordercolor=red";}
if($color9){$color99="bordercolor=red";}

if($hae){$hae1="<form action=\./mydata.cgi\ method=\post\><TR><TH>�ذ�</TH><TD colspan=2>�ڱ��� ����� �ذ��մϴ�.</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM4><input type=hidden name=type value=5><input type=submit value=�ذ�></TH></TR></form>";}
if($hae2){$hae22="<form action=\./mydata.cgi\ method=\post\><TR><TH>����</TH><TH colspan=3><input type=text name=mes size=70></TH><TH align=\"left\"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM2><input type=submit value=����></TH></TR></form>
<form action=\./mydata.cgi\ method=\post\><TR><TH>����ȸ������ ������ �ۼ�</TH><TH colspan=3><input type=text name=mes size=60></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM5><input type=submit value=����></TH></TR></form>";}

	&TIME_DATA;

	&HEADER;
	print <<"EOM";
<TABLE border=0 width=100% height=100%><TR><TD align=center>
<table align="center" border="1" cellspacing="0" width="700" bgcolor=$ELE_BG[$xele]>
    <tr>
        <td width="1101" height="795">
            <table align="center" cellpadding="0" cellspacing="0" width="684">
                <tr>
                    <td width="684" height="25" colspan="6" align="center">
                        <p align="center"><span style="font-size:9pt;"><font face="����">����������</font></span></p>
                    </td>
                </tr>
                <tr>
                    <td width="684" height="113" colspan="6">
                        <table align="center" cellpadding="0" cellspacing="0" width="299">
                            <tr>
                                <td width="142">
                                    <table align="center" border="1" cellspacing="0">
                                        <tr>
                                            <td width="64" height="80" background="$IMG/$king_chara.gif">
                                            </td>
                                        </tr>
                                        <tr>
                                            <td width="64" height="30">
                                                <p align="center">$king_name<br><img src="$IMG/gg01.jpg">
                                            </td></tr>
                                    </table>
                                </td>
                                <td width="141">
                                    <table align="center" border="1" cellspacing="0" width="70" $color11>
                                        <tr>
                                            <td width="64" height="80" background="$ximg[0]">
                                            </td>
                                        </tr>
                                        <tr>
                                            <td width="64" height="30">
                                                <p align="center">$tname[0]<br><img src="$IMG/gg02.jpg">
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td width="50%" height="25" colspan="3">
                        <p align="center"><font face="����"><span style="font-size:9pt;">�屺����</span></font></p>
                    </td>
                    <td width="50%" height="25" colspan="3">
                        <p align="center"><font face="����"><span style="font-size:9pt;">��������</span></font></p>
                    </td>
                </tr>
                <tr>
                    <td width="50%" height="108" colspan="3">
                        <table align="center" border="1" cellspacing="0" width="70" $color11>
                            <tr>
                                <td width="64" height="80" background="$ximg[1]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[1]<br><img src="$IMG/gg03.jpg"></p>
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="50%" height="108" colspan="3">
                        <table align="center" border="1" cellspacing="0" width="70" $color11>
                            <tr>
                                <td width="64" height="80" background="$ximg[17]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[17]<br><img src="$IMG/gg04.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" $color22>
                            <tr>
                                <td width="64" height="80" background="$ximg[2]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[2]<br><img src="$IMG/gg05.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" $color22>
                            <tr>
                                <td width="64" height="80" background="$ximg[3]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[3]<br><img src="$IMG/gg06.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" $color22>
                            <tr>
                                <td width="64" height="80" background="$ximg[4]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[4]<br><img src="$IMG/gg07.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" $color33>
                            <tr>
                                <td width="64" height="80" background="$ximg[18]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[18]<br><img src="$IMG/gg20.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" $color33>
                            <tr>
                                <td width="64" height="80" background="$ximg[19]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[19]<br><img src="$IMG/gg21.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" $color33>
                            <tr>
                                <td width="64" height="80" background="$ximg[20]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[20]<br><img src="$IMG/gg22.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" $color44>
                            <tr>
                                <td width="64" height="80" background="$ximg[5]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[5]<br><img src="$IMG/gg08.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" $color99>
                            <tr>
                                <td width="64" height="80" background="$ximg[9]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[9]<br><img src="$IMG/gg12.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" $color55>
                            <tr>
                                <td width="64" height="80" background="$ximg[13]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[13]<br><img src="$IMG/gg16.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" $color66>
                            <tr>
                                <td width="64" height="80" background="$ximg[21]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[21]<br><img src="$IMG/gg23.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" $color77>
                            <tr>
                                <td width="64" height="80" background="$ximg[23]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[23]<br><img src="$IMG/gg25.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" $color88>
                            <tr>
                                <td width="64" height="80" background="$ximg[25]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[25]<br><img src="$IMG/gg27.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" $color44>
                            <tr>
                                <td width="64" height="80" background="$ximg[6]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[6]<br><img src="$IMG/gg09.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" $color99>
                            <tr>
                                <td width="64" height="80" background="$ximg[10]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[10]<br><img src="$IMG/gg13.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" $color55>
                            <tr>
                                <td width="64" height="80" background="$ximg[14]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[14]<br><img src="$IMG/gg17.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" $color66>
                            <tr>
                                <td width="64" height="80" background="$ximg[22]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[22]<br><img src="$IMG/gg24.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" $color77>
                            <tr>
                                <td width="64" height="80" background="$ximg[24]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[24]<br><img src="$IMG/gg26.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" $color88>
                            <tr>
                                <td width="64" height="80" background="$ximg[26]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[26]<br><img src="$IMG/gg28.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" $color44>
                            <tr>
                                <td width="64" height="80" background="$ximg[7]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[7]<br><img src="$IMG/gg10.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" $color99>
                            <tr>
                                <td width="64" height="80" background="$ximg[11]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[11]<br><img src="$IMG/gg14.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" $color55>
                            <tr>
                                <td width="64" height="80" background="$ximg[15]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[15]<br><img src="$IMG/gg18.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="342" height="130" colspan="3">
                        <p align="center"><span style="font-size:9pt;"><b>�ڽſ��� 
                        �ο������� �ִ� ������</b></span>
                        <p align="center"><span style="font-size:9pt;"><b>�������� 
                        ���������� ���մϴ�.</b></span></p>
</td>
                </tr>
                <tr>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" $color44>
                            <tr>
                                <td width="64" height="80" background="$ximg[8]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[8]<br><img src="$IMG/gg11.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" $color99>
                            <tr>
                                <td width="64" height="80" background="$ximg[12]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[12]<br><img src="$IMG/gg15.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                        <table align="center" border="1" cellspacing="0" width="70" $color55>
                            <tr>
                                <td width="64" height="80" background="$ximg[16]">
                                </td>
                            </tr>
                            <tr>
                                <td width="64" height="30">
                                    <p align="center">$tname[16]<br><img src="$IMG/gg19.jpg">
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td width="16%" height="130">
                    </td>
                    <td width="16%" height="130">
                    </td>
                    <td width="16%" height="130">
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
<TR><TD>

<center><TABLE bgcolor=$TABLE_C><TBODY bgcolor=$TD_C4>

$jjang
$hae1
$hae22
$jjang2
$chset
<form action=\"./mydata.cgi\" method=\"post\"><TR><TH>��������</TH><TD colspan=2>�ڱ� ������ ������ �����մϴ�.</TD><TH><select name=sel>$list2</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM6><input type=hidden name=type value=27><input type=submit value="����"></TH></TR></form>
</TBODY></TABLE>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="���ƿ´�"></form></CENTER>
</TD></TR></TABLE>
</TD></TR></TABLE>

EOM

	&FOOTER;

	exit;

}
1;