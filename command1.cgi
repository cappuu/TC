#!/usr/bin/perl

require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

if($MENTE) { &ERR("�ε����Դϴ�. ��ø� ��ٷ� �ֽʽÿ�."); }
&DECODE;
&COM1;


sub COM1 {


	if($in{'no'} eq ""){&ERR("NO:�� �Էµ��� �ʾҽ��ϴ�.");}
	&CHARA_MAIN_OPEN;
	&CHARA_ITEM_OPEN;
	&TIME_DATA;

	open(IN,"./charalog/command1/$kid.cgi");
	@COM_DATA = <IN>;
	close(IN);

	$mes_num = @COM_DATA;

	if($mes_num > 30) { pop(@COM_DATA); }


	if($in{'mode'} eq 0){
		$comname = "�Ϲݰ���";
		$cpoint = 0;
		$cra = 0;
	}elsif($in{'mode'} eq 1){
		$comname = "������";
		$cpoint = 25;
		$cra = 1;
	}elsif($in{'mode'} eq 2){
		$comname = "����";
		$cpoint = 25;
		$cra = 2;
	}elsif($in{'mode'} eq 3){
		$comname = "�����";
		$cpoint = 25;
		$cra = 3;
	}elsif($in{'mode'} eq 4){
		$comname = "���";
		$cpoint = 75;
		$cra = 1;
	}elsif($in{'mode'} eq 5){
		$comname = "�����";
		$cpoint = 75;
		$cra = 2;
	}elsif($in{'mode'} eq 6){
		$comname = "������";
		$cpoint = 75;
		$cra = 3;
	}elsif($in{'mode'} eq 11){
		$comname = "��ȭ����";
		$cpoint = 150;
		$cra = 1;
	}elsif($in{'mode'} eq 12){
		$comname = "��õ�Ź�";
		$cpoint = 150;
		$cra = 2;
	}elsif($in{'mode'} eq 13){
		$comname = "��õź��";
		$cpoint = 150;
		$cra = 3;
	}elsif($in{'mode'} eq 14){
		$comname = "����͸�";
		$cpoint = 100;
		$cra = 1;
	}elsif($in{'mode'} eq 15){
		$comname = "�Ŷ�˹�";
		$cpoint = 120;
		$cra = 3;
	}elsif($in{'mode'} eq 16){
		$comname = "����";
		$cpoint = 300;
		$cra = 2;
	}elsif($in{'mode'} eq 17){
		$comname = "����";
		$cpoint = 100;
		$cra = 0;
	}elsif($in{'mode'} eq 18){
		$comname = "����ȭ����";
		$cpoint = 350;
		$cra = 1;
	}

	if($kskill =~ /Gb/){
	$ctotal = int((500+($kclass/50)) * 1.2);
	}else{
	$ctotal = 500+int($kclass/50);
	}


	@NEW_COM_DATA=();$i=0;
	if($in{'no'} eq "all"){
		while(@NEW_COM_DATA < 30){
			push(@NEW_COM_DATA,"$comname<>$in{'mode'}<>$cpoint<>$cra<>\n");
			if($i eq $_){
			}else{
			$cpoin1 += $cpoint;
			}
		}
		$no = $in{'no'};
	}else{
		foreach(@COM_DATA){
			($cname,$cno,$cp,$crap) = split(/<>/);
			$ahit=0;

			foreach(@no){
				if($i eq $_){
					$ahit=1;
					push(@NEW_COM_DATA,"$comname<>$in{'mode'}<>$cpoint<>$cra<>\n");
					$lno = $_ + 1;
					$no .= "$lno,";
					$cpoin1 += $cpoint;
				}	
			}

			if(!$ahit){
					$cpoin1 += $cp;
					push(@NEW_COM_DATA,"$_");
			}

			$i++;
		}
	}

		
	if($cpoin1 > $ctotal){
	&ERR("�������Ʈ�� ���ڶ��ϴ�.");
	}

	open(OUT,">./charalog/command1/$kid.cgi") or &ERR('������ ���� �ʾҽ��ϴ�.');
	print OUT @NEW_COM_DATA;
	close(OUT);

	&HEADER;

	print <<"EOM";

<CENTER><hr size=0><h2>����Ŀ�ǵ� $no�Ͽ� $comname�� �Է��Ͽ����ϴ�. CP: $cpoin1/$ctotal</h2><p>
<form action="setting.cgi" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=TOP>
<script language="javascript">
setTimeout(form.submit(), 1);
</script>
<input type=submit value="Ȯ��"></form>


</CENTER>
EOM

	&FOOTER;

	exit;

}