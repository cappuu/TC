#!/usr/bin/perl

require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

if($MENTE) { &ERR("�ε����Դϴ�. ��ø� ��ٷ� �ֽʽÿ�."); }
&DECODE;
&TOP;

sub TOP {

	&CHARA_MAIN_OPEN;
	open(IN,"./charalog/log/$kid.cgi");
	@LOG_DATA = <IN>;
	close(IN);
	&TOWN_DATA_OPEN($kpos);
	&COUNTRY_DATA_OPEN($kcon);

	$p=0;
	foreach(@LOG_DATA){
		$log_list .= "<font color=navy>��</font>$LOG_DATA[$p]<BR>";$p++;
	}

	opendir(dirlist,"./charalog/main");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"./charalog/main/$file")){
				&ERR2("���� ���� ����!");
			}
			@page = <page>;
			close(page);
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);

	$list = "<TBODY bgcolor=$ELE_C[$xele]><TR><TD align=center></TD><TH>�̸�</TH><TH>����</TH><TH>����</TH><TH>��ַ�</TH><TH>�ŷ�</TH><TH>����</TH><TH>�����</TH><TH>����</TH><TH>���</TH></TR>";
	$num=0;


	foreach(@CL_DATA){
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint) = split(/<>/);
		($estr_ex,$eint_ex,$elea_ex,$echa_ex,$esub1_ex,$esub2_ex) = split(/,/,$esub1);

		if($epos eq $kpos){
			$num++;
			$com_list = "";
			if($kcon eq $econ){
				open(IN,"./charalog/command/$eid.cgi");
				@COM_DATA = <IN>;
				close(IN);
				for($i=0;$i<$MAX_COM;$i++){
					($cid,$cno,$cname,$ctime,$csub,$cnum,$cend) = split(/<>/,$COM_DATA[$i]);
					$no = $i+1;
					if($cid eq ""){
					$com_list .= "$no: - <BR>";
					}else{
					$com_list .= "$no:$cname<BR>";
					}
					if($i>=3){last;}
				}
			}

			if($num < 100){
			$list .= "<TR><TD align=center><img src=$IMG/$echara.gif></TD><TD width=80><center><a href=\"javascript:info('$eid')\">$ename</a></TD><TD width=50><center>$estr</TD><TD width=50><center>$eint</TD><TD width=50><center>$elea</TD><TD width=50><center>$echa</TD><TD width=50><center>$SOL_TYPE[$esub1_ex]</TD><TD width=50><center>$esol��</TD><TD width=50><center>$cou_name[$econ]��</TD><TD>$com_list</TD></TR>";
			}
		}
	}
	&HEADER;
	print <<"EOM";
<body bgcolor="white" text="white" link="blue" vlink="purple" alink="red" leftmargin="0" marginwidth="0" topmargin="0" marginheight="0">
<table align="center" cellpadding="0" cellspacing="0" width="945">
    <tr>
        <td width="945">
            <p><img src="$IMG/up.gif" width="950" height="93" border="0"></p>
        </td>
    </tr>
    <tr>
        <td width="945" height="857" background="$IMG/backg.gif"><br>
            <table align="center" cellpadding="0" cellspacing="0" width="700">
                <tr>
                    <td width="940">
                        <p><img src="$IMG/law1.gif" width="700" height="22" border="0"></p>
                    </td>
                </tr>
                <tr>
                    <td width="940" height="785" background="$IMG/law3.gif">
<CENTER>
<br>
<TABLE WIDTH="95%" height=100% cellpadding="0" cellspacing="0" border=0><tr><td align=center>
<B>��$zname������ Ÿ���� ���� $num���� ������� �ֵ����Դϴ�.��</b>
<TABLE border=0 cellspacing=1 bgcolor=$TABLE_C>
    <TBODY bgcolor=FFFFFF>
$list
</TBODY></TABLE>
<BR>
<TABLE border=0 cellspacing=1>
<TBODY><TR><TD>
$log_list
</TD></TR>
</TBODY></TABLE>
<form action=\"$FILE_STATUS\" method=\"post\"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=STATUS><input type=submit value=\"���ƿ´�\">
</form>

</TD></TR>
</TBODY></TABLE><br>                    </td>
                </tr>
                <tr>
                    <td width="940">
                        <p><img src="$IMG/law2.gif" width="700" height="22" border="0"></p>
                    </td>
                </tr>
            </table><br>
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

