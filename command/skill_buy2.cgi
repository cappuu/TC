sub SKILL_BUY2 {

	if($in{'no'} eq ""){&ERR("NO:�� �Էµ��� �ʾҽ��ϴ�.");}
	if($in{'select'} eq ""){&ERR("Ư�Ⱑ �Էµ��� �ʾҽ��ϴ�.");}
	&CHARA_MAIN_OPEN;
	open(IN,"$SKILL_LIST") or &ERR('������ ���� �ʾҽ��ϴ�.');
	@SKILL_DATA = <IN>;
	close(IN);

	$num = $in{'select'};
	($dk,$eskillcode,$eskillpoint) = split(/<>/,$SKILL_DATA[$num]);

	$hit=0;

	if($eskillcode =~ /Ab/ && $kskill !~ /Aa/){&ERR("Ư�� �ŷ��� ���� ���ؼ��� ���� ����� ���ž� �մϴ�.");}
	if($eskillcode =~ /Ac/ && $kskill !~ /Ab/){&ERR("Ư�� ������ ���� ���ؼ��� ���� �ŷ��� ���ž� �մϴ�.");}
	if($eskillcode =~ /Bb/ && $kskill !~ /Ba/){&ERR("Ư�� ������ ���� ���ؼ��� ���� ����� ���ž� �մϴ�.");}
	if($eskillcode =~ /Bc/ && $kskill !~ /Bb/){&ERR("Ư�� ����� ���� ���ؼ��� ���� ������ ���ž� �մϴ�.");}
	if($eskillcode =~ /Cb/ && $kskill !~ /Ca/){&ERR("Ư�� ȸ�Ǹ� ���� ���ؼ��� ���� ����� ���ž� �մϴ�.");}
	if($eskillcode =~ /Cc/ && $kskill !~ /Ca/){&ERR("Ư�� ������ ���� ���ؼ��� ���� ȸ�Ǹ� ���ž� �մϴ�.");}
	if($eskillcode =~ /Db/ && $kskill !~ /Da/){&ERR("Ư�� ���� ���� ���ؼ��� ���� �缺�� ���ž� �մϴ�.");}
	if($eskillcode =~ /Dc/ && $kskill !~ /Db/){&ERR("Ư�� ��ġ�� ���� ���ؼ��� ���� ���� ���ž� �մϴ�.");}
	if($eskillcode =~ /Eb/ && $kskill !~ /Ea/){&ERR("Ư�� ������ ���� ���ؼ��� ���� �Ʒ��� ���ž� �մϴ�.");}
	if($eskillcode =~ /Ec/ && $kskill !~ /Eb/){&ERR("Ư�� ������ ���� ���ؼ��� ���� ������ ���ž� �մϴ�.");}
	if($eskillcode =~ /Fb/ && $kskill !~ /Fa/){&ERR("Ư�� �ŷḦ ���� ���ؼ��� ���� �ν��� ���ž� �մϴ�.");}
	if($eskillcode =~ /Fc/ && $kskill !~ /Fb/){&ERR("Ư�� ������ ���� ���ؼ��� ���� �ŷḦ ���ž� �մϴ�.");}
	if($eskillcode =~ /Gb/ && $kskill !~ /Ga/){&ERR("Ư�� ������ ���� ���ؼ��� ���� ����� ���ž� �մϴ�.");}
	if($eskillcode =~ /Gc/ && $kskill !~ /Gb/){&ERR("Ư�� �ϼ��� ���� ���ؼ��� ���� ������ ���ž� �մϴ�.");}

	if($eskillcode =~ /Aa/ && $kskill =~ /Aa/){&ERR("�̹� ����� ���̽��ϴ�.");}
	if($eskillcode =~ /Ab/ && $kskill =~ /Ab/){&ERR("�̹� �ŷ��� ���̽��ϴ�.");}
	if($eskillcode =~ /Ac/ && $kskill =~ /Ac/){&ERR("�̹� ������ ���̽��ϴ�.");}
	if($eskillcode =~ /Ba/ && $kskill =~ /Ba/){&ERR("�̹� ����� ���̽��ϴ�.");}
	if($eskillcode =~ /Bb/ && $kskill =~ /Bb/){&ERR("�̹� ������ ���̽��ϴ�.");}
	if($eskillcode =~ /Bc/ && $kskill =~ /Bc/){&ERR("�̹� ����� ���̽��ϴ�.");}
	if($eskillcode =~ /Ca/ && $kskill =~ /Ca/){&ERR("�̹� ����� ���̽��ϴ�.");}
	if($eskillcode =~ /Cb/ && $kskill =~ /Cb/){&ERR("�̹� ȸ�Ǹ� ���̽��ϴ�.");}
	if($eskillcode =~ /Cc/ && $kskill =~ /Cc/){&ERR("�̹� ������ ���̽��ϴ�.");}
	if($eskillcode =~ /Da/ && $kskill =~ /Da/){&ERR("�̹� �缺�� ���̽��ϴ�.");}
	if($eskillcode =~ /Db/ && $kskill =~ /Db/){&ERR("�̹� ���� ���̽��ϴ�.");}
	if($eskillcode =~ /Dc/ && $kskill =~ /Dc/){&ERR("�̹� ��ġ�� ���̽��ϴ�.");}
	if($eskillcode =~ /Ea/ && $kskill =~ /Ea/){&ERR("�̹� �Ʒ��� ���̽��ϴ�.");}
	if($eskillcode =~ /Eb/ && $kskill =~ /Eb/){&ERR("�̹� ������ ���̽��ϴ�.");}
	if($eskillcode =~ /Ec/ && $kskill =~ /Ec/){&ERR("�̹� ������ ���̽��ϴ�.");}
	if($eskillcode =~ /Fa/ && $kskill =~ /Fa/){&ERR("�̹� �ν��� ���̽��ϴ�.");}
	if($eskillcode =~ /Fb/ && $kskill =~ /Fb/){&ERR("�̹� �ŷḦ ���̽��ϴ�.");}
	if($eskillcode =~ /Fc/ && $kskill =~ /Fc/){&ERR("�̹� ������ ���̽��ϴ�.");}
	if($eskillcode =~ /Ga/ && $kskill =~ /Ga/){&ERR("�̹� ����� ���̽��ϴ�.");}
	if($eskillcode =~ /Gb/ && $kskill =~ /Gb/){&ERR("�̹� ������ ���̽��ϴ�.");}
	if($eskillcode =~ /Gc/ && $kskill =~ /Gc/){&ERR("�̹� �ϼ��� ���̽��ϴ�.");}

	if($kpoint < $eskillpoint){&ERR("Ư�� ����Ʈ�� �����մϴ�.");}

	open(IN,"./charalog/command/$kid.cgi");
	@COM_DATA = <IN>;
	close(IN);

	if($in{'select'} eq 0){
	$name = '���';
	}
	if($in{'select'} eq 1){
	$name = '�ŷ�';
	}
	if($in{'select'} eq 2){
	$name = '����';
	}
	if($in{'select'} eq 3){
	$name = '���';
	}
	if($in{'select'} eq 4){
	$name = '����';
	}
	if($in{'select'} eq 5){
	$name = '���';
	}
	if($in{'select'} eq 6){
	$name = '���';
	}
	if($in{'select'} eq 7){
	$name = 'ȸ��';
	}
	if($in{'select'} eq 8){
	$name = '����';
	}
	if($in{'select'} eq 9){
	$name = '�缺';
	}
	if($in{'select'} eq 10){
	$name = '��';
	}
	if($in{'select'} eq 11){
	$name = '��ġ';
	}
	if($in{'select'} eq 12){
	$name = '�Ʒ�';
	}
	if($in{'select'} eq 13){
	$name = '����';
	}
	if($in{'select'} eq 14){
	$name = '����';
	}
	if($in{'select'} eq 15){
	$name = '�ν�';
	}
	if($in{'select'} eq 16){
	$name = '�ŷ�';
	}
	if($in{'select'} eq 17){
	$name = '����';
	}
	if($in{'select'} eq 18){
	$name = '���';
	}
	if($in{'select'} eq 19){
	$name = '����';
	}
	if($in{'select'} eq 20){
	$name = '�ϼ�';
	}

	$mes_num = @COM_DATA;

	if($mes_num > $MAX_COM) { pop(@COM_DATA); }

	@NEW_COM_DATA=();$i=0;

	if($in{'no'} eq "all"){
		while(@NEW_COM_DATA < $MAX_COM){
			push(@NEW_COM_DATA,"$in{'mode'}<><>Ư�� $name�� ����.<>$tt<><>$num<><>\n");
		}
		$no = $in{'no'};
	}else{
		foreach(@COM_DATA){
			($cid,$cno,$cname,$ctime,$csub,$cnum,$cend) = split(/<>/);
			$ahit=0;
			foreach(@no){
				if($i eq $_){
					$ahit=1;
					push(@NEW_COM_DATA,"$in{'mode'}<><>Ư�� $name�� ����<>$tt<><>$num<><>\n");
					$lno = $_ + 1;
					$no .= "$lno,";
				}
			}
			if(!$ahit){
				push(@NEW_COM_DATA,"$_");
			}
			$i++;
		}
	}

	open(OUT,">./charalog/command/$kid.cgi") or &ERR('������ ���� �ʾҽ��ϴ�.');
	print OUT @NEW_COM_DATA;
	close(OUT);

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>NO:$no�� Ư�� $name�� ������� �Է��߽��ϴ�.</h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="Ȯ��"></form></CENTER>
EOM

	&FOOTER;

	exit;

}
1;