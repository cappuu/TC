#!/usr/bin/perl

require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

&DECODE;
if( $in{'mode'} eq "edit" ){
	&EDIT;
}elsif( $in{'mode'} eq "passwd" ){
	&PASSWD;
}else{
	&TOP;
}

sub TOP {

	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN($kpos);
	&COUNTRY_DATA_OPEN($kcon);
	&CHARA_ITEM_OPEN;

	if( $in{'ins'} ne ""){
		$mes = $in{'ins'};
		$mes =~ s/<br>/\n/ig;
	}else{
		$mes = $kmes;
		$mes =~ s/<br>/\n/ig;
	}

	&HEADER;


	if($kskill =~ /Gb/){
	$ctotal = int((500+($kclass/50)) * 1.2);
	}else{
	$ctotal = 500+int($kclass/50);
	}

	open(IN,"./charalog/command1/$kid.cgi");
	@COM_DATA = <IN>;
	close(IN);

	foreach(@COM_DATA){
	($cname,$cno,$cp,$crap)=split(/<>/);
		$cpoin += $cp;
	}

	print <<"EOM";

	<script language="JavaScript">
		function changeImg(){
			num=document.para.mode.selectedIndex;
			document.Img.src="$IMG/jensul"+ num +".jpg";
		}
	</script>
<body bgcolor="white" text="white" link="blue" vlink="purple" alink="red" leftmargin="0" marginwidth="0" topmargin="0" marginheight="0">
<table align="center" cellpadding="0" cellspacing="0" width="945">
    <tr>
        <td width="945">
            <p><img src="$IMG/up.gif" width="950" height="93" border="0"></p>
        </td>
    </tr>
    <tr>
        <td width="945" height="740" background="$IMG/backg.gif">
            <table align="center" cellpadding="0" cellspacing="0" width="700">
                <tr>
                    <td width="940">
<p align="center">&nbsp;</p>
                        <p><img src="$IMG/law1.gif" width="700" height="22" border="0"></p>
                    </td>
                </tr>
                <tr>
                    <td width="940" height="522" background="$IMG/law3.gif">
                            <table align="center" border="1" cellspacing="0" width="694" bordercolordark="white" bordercolorlight="black">
                                <tr>
                                    <td  width=200 height="424" rowspan="2">
EOM

	open(IN,"./charalog/command1/$kid.cgi");
	@COM_DATA = <IN>;
	close(IN);

for($i=0;$i<30;$i++){
($cname,$cno,$cp,$crap) = split(/<>/,$COM_DATA[$i]);
		$no = $i+1;
		if($cno eq "" || $cno eq 0){
			$com_list .= "<TR height=20><TH width=30>$no��</TH><TH width=100>�Ϲݰ���</TH></TR>";
		}else{
			$com_list .= "<TR height=20><TH width=30>$no��</TH><TH width=100>$cname</TH></TR>";
		}
	}

print <<"EOM";


<TABLE bgcolor=$TABLE_C cellspacing=1><TBODY BGCOLOR=$TD_C2>
<TR><th colspan=2>���� �Է� Ŀ�ǵ�</th></TR>
<TR><th colspan=2>����Ʈ $cpoin/$ctotal</th></TR>
$com_list
</TABLE>
                                    </td>

<form action="./command1.cgi" method="POST" name=para>
                                    <td width="479" height="13">
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>

<table>
    <tr>
        <td rowspan="2">
<select name=no size="6" MULTIPLE style="color:rgb(204,204,0); background-color:rgb(93,40,0);">
<option value="all">ALL
EOM
	for($i=0;$i<30;$i++){
		$no = $i+1;
		if($i eq "0"){
		print "<option value=\"$i\" SELECTED>$no��";
		}else{
		print "<option value=\"$i\">$no��";
		}
	}
print <<"EOM";
</select>
        </td>
        <td colspan="2">
<p align="center"><img src=\"$IMG/jensul0.jpg\" name=\"Img\"></p>
        </td>
    </tr>
    <tr>
        <td>
<select name=mode style="font-size:9pt;" onChange=\"changeImg()\" size=1>
<option value="0">�Ϲݰ���
<option style="color:#000000;background-color:#C7FFC9;" value="1">������ [����(����) / ��10% / ��10% / CP25]
<option style="color:#000000;background-color:#C7FFC9;" value="2">���� [����(����) / ��10% / ��10% / CP25]
<option style="color:#000000;background-color:#C7FFC9;" value="3">����� [�л�(��) / ��10% / ��10% / CP25]
<option style="color:#000000;background-color:#AEAE48;" value="4">��� [����(����) / ��15% / ��12% / CP75]
<option style="color:#000000;background-color:#AEAE48;" value="5">����� [����(����) / ��15% / ��12% / CP75]
<option style="color:#000000;background-color:#AEAE48;" value="6">������ [�л�(��) / ��15% / ��12% / CP75]
<option style="color:#000000;background-color:#CC3399;" value="14">������� [����(����) / ��20% / ��12% / CP100 / �űͺ�]
<option style="color:#000000;background-color:#CC3399;" value="11">��ȭ�� [����(����) / ��28% / ��15% / CP150 / ��ȭ�ſ���]
<option style="color:#000000;background-color:#CC3399;" value="12">��õ�� [����(����) / ��18% / ��12% / CP170 / õ�ص� / ����� �����ݡ�]
<option style="color:#000000;background-color:#CC3399;" value="16">������ [����(����) / ��15% / ��8% / CP300 / Ȳ�ٺ� / ����� ����ȸ��]
<option style="color:#000000;background-color:#CC3399;" value="13">ź���� [�л�(��) / ��22% / ��15% / CP150 / ��ͳ��� / ���Ƿε���]
<option style="color:#000000;background-color:#CC3399;" value="15">�Ŷ���� [�л�(��) / ��15% / ��12% / CP120 / ȭ�� / �Ʒõ� -5�� �϶�]
</select>
        </td>
        <td>
<input type=submit style="font-family:�ü�; color:$ELE_C[$xele]; background-color:$ELE_BC[$xele]; border-width:1; border-color:black; border-style:solid;" value="����">
        </td>
</form>
    </tr>
</table>
                                    </td>
                                </tr>
                                <tr>
                                    <td width="550" height="411" valign="up">

<table border="1" width="100%">
    <tr>
        <td width="100%" border="0" cellspacing="1" cellpadding="2" bgcolor=black>
            <p><b>[���� Ŀ�ǵ� �ý��� �̿���]</b><br>�ڽ��� �־��� ��������Ʈ(CP)�� 
            �ѵ������� ������ ¬�ϴ�.<br>������ �ϳ� �߰��� ������ ��ħ�޴�â�� 
            ǥ�õ� CP��ŭ �Ҹ�Ǹ� �¸��� ����Ǵ� �������ۼ�Ʈ�� �й�� ����Ǵ� 
            �������ۼ�Ʈ�� ǥ�õ˴ϴ�.<br>CP�� �Ѱ���ġ�� ������ ������ �Ѱ���ġ�� 
            �þ���� ������ �� �ִ� ������ ���ܳ��ϴ�.<br>�������� <b>����(����) 
            &gt;&nbsp;�л�(��) &gt; ����(����) &gt; ����(����) </b>�̸� �̱�ų� 
            ���ų� ��� �� �ֽ��ϴ�.<br>��, �Ϲݰ����� ��� �󼺿��� �ݵ�� �й������� ���� Ư������(��ų)�� ������ ���� �ʽ��ϴ�..<br><b>��CP�� �ѹ����� �������� �Ҹ�����Ʈ�� �ƴմϴ�.</b></p>
        </td>
    </tr>
</table>
<br>
<form action="setting.cgi" method="post">
<input type=hidden name=mode value="edit">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
	<table width="100%" border="0" cellspacing="1" cellpadding="2" bgcolor=$ELE_BG[$cou_ele[$kcon]]>
	<tr bgcolor=$ELE_C[$cou_ele[$kcon]]>
	<td width="200">���� �ڱ�Ұ�<br>(���� 100�ڱ���)</td>
	<td width="300">$kmes<br><textarea name="ins" cols="40" rows="5">$mes</textarea>
	</td>
	</tr>
    <tr>
	<td width="1105" colspan="2">
            <p align="center"><input type="submit" value="����">
</td>
		</form>
    </tr>
	</table>
<br>
<form action="setting.cgi" method="post">
<input type=hidden name=mode value="passwd">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
	<table width="100%" border="0" cellspacing="1" cellpadding="2" bgcolor=$ELE_BG[$cou_ele[$kcon]]>
	<tr bgcolor=$ELE_C[$cou_ele[$kcon]]>
	<td width="100">�н����� ����</td>
	<td width="308"><input type=text name=newpass value="" size="10" maxlength="8">[�ݰ������ڷ� 4~8���� �̳�]
	</td>
	<td width="76">
<input type="submit" value="����">
	</td>
</form>
	</tr>
	</table>
<br>
<form action="backup.cgi" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=BAK>
<p align="center"><input type=submit value="�����͹��(�Ϸ翡 �ѹ��� ����)"></p></form>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<p align="center"><input type=submit value="Ȯ��"></p></form>
                                    </td>
                                </tr>
                            </table>
                        <p>&nbsp;</p>
                    </td>
                </tr>
                <tr>
                    <td width="940">
                        <p><img src="$IMG/law2.gif" width="700" height="22" border="0"></p>
                    </td>
                </tr>
            </table>
            <p>&nbsp;</p>
        </td>
    </tr>
    <tr>
        <td width="945">
            <p><img src="$IMG/down.gif" width="950" height="26" border="0"></p>
        </td>
    </tr>
</table>
</body>

EOM

	&FOOTER;
	exit;

}

sub EDIT {
	&CHARA_MAIN_OPEN;

	$ins = $in{'ins'};
	if( length($ins) > 200){
		&TOP("���� : ���� 100�ڸ� �Ѿ���Ƚ��ϴ�.");
	}
	$kmes = $ins;
	&CHARA_MAIN_INPUT;

	&HEADER;
	print <<"EOM";
<CENTER><hr size=0><h2>������ �Ϸ��߽��ϴ�.</h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="Ȯ��"></form></CENTER>
EOM

	&FOOTER;
	exit;

}

sub BAK {
	&CHARA_MAIN_OPEN;

	open(IN,"./charalog/bak/$in{'id'}.cgi");
	@KK = <IN>;
	close(IN);

	($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$kskill,$kpoint,$kct,$klevel,$kexp,$kcodea,$kcodeb,$kqpoint) = split(/<>/);

	open(OUT,">./charalog/bak/$in{'id'}.cgi");
	print OUT @KK;
	close(OUT);

	&HEADER;
	print <<"EOM";
<CENTER><hr size=0><h2>$in{'id'}���� �����͸� ����߽��ϴ�.</h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="Ȯ��"></form></CENTER>

EOM

	&FOOTER;
	exit;
}




sub PASSWD {
	&CHARA_MAIN_OPEN;

	if ($in{'newpass'} =~ m/[^0-9a-zA-Z]/) {&TOP("","���� : �н����忡 �ݰ������� �̿��� ���ڰ� ���ԵǾ� �ֽ��ϴ�."); }
	elsif($in{'newpass'} eq "" || length($in{'newpass'}) < 4 || length($in{'newpass'}) > 8) { &TOP("","���� : 4���� �̻� 8���� ���Ϸ� �Է����ּ���."); }
	$kpass = $in{'newpass'};
	&CHARA_MAIN_INPUT;

	&HEADER;
	print <<"EOM";
<CENTER><hr size=0><h2>�н����带 �����߽��ϴ�.</h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="Ȯ��"></form></CENTER>

EOM

	&FOOTER;
	exit;

}


