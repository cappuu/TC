#_/_/_/_/_/_/_/_/_/_/_/#
#_/    ���� ȭ��    _/#
#_/_/_/_/_/_/_/_/_/_/_/#

sub tenka {

	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&COUNTRY_DATA_OPEN("$kcon");
	&CHARA_ITEM_OPEN;
	&TIME_DATA;

	open(IN,"./data/entry_list.cgi") or &error("����� ����Ʈ�� ������ �ʽ��ϴ�.");
	@ENTRY = <IN>;
	close(IN);
	$ent=0;
	$entcount=@ENTRY;
	@N_ENTRY=();
	foreach(@ENTRY){
		($tid,$tname,$tchara,$tcon,$tcname,$tcele,$tpoint,$tflg) =split(/<>/);
		if($ent>1){push(@N_ENTRY,"$_");}
		$ent++;
	}
	($wid,$wname,$wchara,$wcon,$wcname,$wcele,$wpoint,$wflg) =split(/<>/,$ENTRY[0]);
	($eid,$ename,$echara,$econ,$ecname,$ecele,$epoint,$eflg) =split(/<>/,$ENTRY[1]);

	
	open(IN,"./data/battle_time.cgi") or &error("Ÿ�� �����Ͱ� ������ �ʽ��ϴ�.");
	@CTIME = <IN>;
	close(IN);
	($ctime,$ccount,$ctotal,$clast,$cflg) =split(/<>/,$CTIME[0]);
	if($ccount eq""){$ccount=1;}
	else{$ccount=1;}
	$ctime=time();

	open(IN,"./data/winner_list.cgi") or &error("Ÿ�� �����Ͱ� ������ �ʽ��ϴ�.");
	@WIN = <IN>;
	close(IN);
	$ceno=@WIN+1;

	if($entcount<=2){
		$cbtype="���";
		&maplog("<font color=orange>[õ�� ���� ���]</font>�������$wname VS $ename�� ������ �߽��ϴ�!");
	}elsif($entcount<=4){
		$cbtype="�ذ��";
		&maplog("<font color=orange>[õ�� ���� �ذ�]</font>�ذ�£�$wname VS $ename�� ������ �߽��ϴ�!");
	}else{
		$cbtype="��$ceno ����";
		&maplog("<font color=green>[õ�� ����]</font>��$ceno ���գ�$wname VS $ename�� ������ �߽��ϴ�!");
	}
	&gprint;
	$turn=0;$win=0;$lose=0;
	while($turn<=30){
		$turn++;
		if($turn>100){&error("����");}
		$bmess="";$bmess1="";$bmess2="";

		if($wab[15] && $wabdmg[15]>$eabdmg[15] && int(rand(3-$wabdmg[15])) eq 0){$sensei = 1;}
		elsif($eab[15] && $eabdmg[15]>$wabdmg[15] && int(rand(3-$eabdmg[15])) eq 0){$sensei = 0;}
		elsif(int(rand($wdex)) > int(rand($edex))){$sensei = 1;}
		else{$sensei = 0;}
		
		if($sensei){
			if($whp>0){
				&wat;
				$bmess.="<table border=0 width=100%><td bgcolor=$ELE_C[2]>$bmess1</td></table>";
			}
			if($ehp>0){
				&eat;
				$bmess.="<table border=0 width=100%><td bgcolor=$ELE_C[1]>$bmess2</td></table>";
			}
		}else{
			if($ehp>0){
				&eat;
				$bmess.="<table width=100%><td bgcolor=$ELE_C[1]>$bmess2</td></table>";
			}if($whp>0){
				&wat;
				$bmess.="<table width=100%><td bgcolor=$ELE_C[2]>$bmess1</td></table>";
			}
		}
		if($win){
			$win_name="$wname";
			$win_id="$wid";
			$lose_name="$ename";
			$lose_id="$eid";

			&bprint;
			push(@N_ENTRY,"$wid<>$wname<>$wchara<>$wcon<>$wcname<>$wcele<>$wpoint<>$wflg<>\n");
			push(@WIN,"$wid<>$wchara<>$wname<>$ename<>$wcon<>$cbtype<>$ctime<>\n");
			$blog.= <<"EOF";
			<center>
			<TABLE border="0" width="400" bgcolor="#000000" CLASS=TC>
  			<TBODY><TR>
      			<TD colspan="2" align="center" bgcolor="$FCOLOR"><FONT color="#ffffcc">���� ����!</FONT></TD>
    			</TR>
    			<TR><TD colspan="2" align="center" bgcolor="$FCOLOR2"><FONT color="#cc0000">$wname</FONT>�� �¸�!<BR>
      			</TD></TR>
  			</TBODY></TABLE>
			</center>
EOF
			last;
		}if($lose){
			$win_name="$ename";
			$win_id="$eid";
			$lose_name="$wname";
			$lose_id="$wid";

			&bprint;
			push(@N_ENTRY,"$eid<>$ename<>$echara<>$econ<>$ecname<>$ecele<>$epoint<>$eflg<>\n");
			push(@WIN,"$eid<>$echara<>$ename<>$wname<>$wcon<>$cbtype<>$ctime<>\n");
			$blog.= <<"EOF";
			<center>
			<TABLE border="0" width="400" bgcolor="#000000" CLASS=TC>
  			<TBODY><TR>
      			<TD colspan="2" align="center" bgcolor="$FCOLOR"><FONT color="#ffffcc">���� ����!</FONT></TD>
    			</TR>
    			<TR><TD colspan="2" align="center" bgcolor="$FCOLOR2"><FONT color="#cc0000">$ename</FONT>�� �¸�!<BR>
      			</TD></TR>
  			</TBODY></TABLE>
			</center>
EOF
			last;
		}
		&bprint;
	}
	if(!$win && !$lose){
		$win_name="$wname";
		$win_id="$wid";
		$lose_name="$ename";
		$lose_id="$eid";

		push(@N_ENTRY,"$wid<>$wname<>$wchara<>$wcon<>$wcname<>$wcele<>$wpoint<>$wflg<>\n");
		push(@WIN,"$wid<>$wchara<>$wname<>$ename<>$wcon<>$cbtype<>$ctime<>\n");
		$bmess.="������ ���� �ʾҴ�.";
		&bprint;
	}
	if(@N_ENTRY<=1){
		&maplog("<font color=red>[��ȸ ���]</font>$win_name�� õ�� ���� ����ȸ���� ����߽��ϴ�!������� �ؼ� �������$win_name���� 500�� Gold,�ؿ����$lose_name���� 200�� Gold�� �־������ϴ�.");
		$enemy_id="$win_id";
		&enemy_open;
		$ebank+=5000000;
		&enemy_input;

		$enemy_id="$lose_id";
		&enemy_open;
		$ebank+=2000000;
		&enemy_input;

		$ccount=0;
		$ctotal++;
		$cflg=0;
	}
	&log_print;

	open(OUT,">./data/winner_list.cgi") or &error('�����͸� �� �� �����ϴ�.');
	print OUT @WIN;
	close(OUT);

	open(OUT,">./data/entry_list.cgi") or &error('�����͸� �� �� �����ϴ�.');
	print OUT @N_ENTRY;
	close(OUT);

	@N_TIMEDATA=();
	push(@N_TIMEDATA,"$ctime<>$ccount<>$ctotal<>$clast<>$cflg<>\n");
	open(OUT,">./data/battle_time.cgi") or &error('�����͸� �� �� �����ϴ�.');
	print OUT @N_TIMEDATA;
	close(OUT);
}

sub wat{
	if(!$wpara2){
		if($wab[1]){
			$hpsai=int($wabdmg[1]/100*$wmaxhp);
			$whp+=$hpsai;
			if($whp>$wmaxhp){$whp=$wmaxhp;}
			$bmess.="[���]$wname�� HP��<font color=blue>$hpsai</font>ȸ���ߴ�.<BR>";
		}

		$wkai = int($wspeed/100 + rand($wspeed/100)) + 1;
		if($wkai<1){$wkai=1;}
		if($wkai>=8){$wkai=8;}

		$bmess.="<font color=blue>$wname</font>��$wkaiȸ����!<BR>";
		if($wpara){
			$whpd=int(rand($wmaxhp*$wpara/10));
			$whp-=$whpd;
			if($whp<=1){$whp=1;}
			$bmess.="<font color=red>���� ����$whpd�� �������� �޾Ҵ�.</font><BR>";
		}
	
		for($kou=0;$kou<$wkai;$kou++){
			$rand=int(rand(100)) ;$at=0;$wsv=0;
			if($wmp/($wmaxmp+1)*100<=$wmprate){$magic=1;}
			elsif($whp/($wmaxhp+1)*100<=$whprate){$magic=2;}
			else{$magic=0;}
			##��� �ߵ�
			$mpdown=$wtec_mp[$magic];
			if($wab[6]){$mpdown-=int($wtec_mp[$magic]*$wabdmg[6]/100);}

			if($wab[25]){
				$whitup=1.5;
			}else{
				$whitup=1;
			}

			if($wtec_hit[$magic]*$whitup>$rand && $mpdown<=$wmp){
				$bmess.="<font color=red size=4><b>$wtec_name[$magic] </b></font>";
				if($wab[6]){$bmess.="<font color=blue><b>(�Һ� $wabdmg[6]%�氨)</b></font>";}
				$wmp-=$mpdown;
				if($wtec_sta[$magic] eq 1){
					$whpup=$wtec_str[$magic] + int(rand($wfai/2));
					$whp+=$whpup;
					if($whp>$wmaxhp){$whp=$wmaxhp;}
					$bmess.="HP��<font color=blue>$whpup</font>ȸ���ߴ�.<BR>";
				}elsif($wtec_sta[$magic] eq 2){
					$whp+=int($wmaxhp/10);
					$wmp+=int($wmaxmp/10);
					if($whp>$wmaxhp){$whp=$wmaxhp;}
					if($wmp>$wmaxmp){$wmp=$wmaxmp;}
					$bmess.="<font color=blue>HP�� MP�� ȸ���ߴ�.</font><BR>";
				}elsif($wtec_sta[$magic] eq 3){
					$wat+=int($wfai*($wtec_str[$magic]/100));
					$bmess.="<font color=blue>���ݷ��� ����ߴ�.</font><BR>";
				}elsif($wtec_sta[$magic] eq 4){
					$wdef+=int($wfai*($wtec_str[$magic]/100));
					$bmess.="<font color=blue>�������� ����ߴ�.</font><BR>";
				}elsif($wtec_sta[$magic] eq 5){
					$wmdef+=int($wfai*($wtec_str[$magic]/100));
					$bmess.="<font color=blue>���� �������� ����ߴ�.</font><BR>";
				}elsif($wtec_sta[$magic] eq 6){
					$wdmg=$etec_str[$magic] + int(rand($wint)) -int($emdef);
					$wsv=6;
					$at=1;
				}elsif($wtec_sta[$magic] eq 7){
					$wsmp=int(rand($emaxmp)/5);
					$emp-=$wsmp;
					if($emp<0){$emp=0;}
					$wmp+=$wsmp;
					if($wmp>$wmaxmp){$wmp=$wmaxmp;}
					$bmess.="$ename�� MP��<font color=red>$wsmp</font>���ѾҴ�.<BR>";
				}elsif($wtec_sta[$magic] eq 8){
					$ehp=int($ehp-$ehp/$wtec_str[$magic]);
					$bmess.="$ename�� ü���� $wtec_str[$magic]���� 1 �����ߴ�.<BR>";
				}else{
					$wdmg=$wtec_str[$magic] + int(rand($wint)) -int($emdef);
					if($wab[5]){
						$wdmg+=int($wdmg*$wabdmg[5]/100);
						$bmess.="<font color=blue><b>(������ +$wabdmg[5]%) </b></font>";
					}
					if($eab[7]){
						$wdmg-=int($wdmg*$eabdmg[7]/100);
						$bmess.="<font color=blue><b>(������-$eabdmg[7]%) </b></font>";
					}
					$at=1;
					if($wtec_sta[$magic] eq 9){$wsv=1;$at=1;}#���
					if($wtec_sta[$magic] eq 10){$wsv=2;$at=1;}#��� �ٿ�
					if($wtec_sta[$magic] eq 11){$wsv=3;$at=1;}#��
					if($wtec_sta[$magic] eq 12){$wsv=4;$at=1;}#���� �ٿ�
					if($wtec_sta[$magic] eq 13){$wsv=5;$at=1;}#����
					if($wtec_sta[$magic] eq 14){$wsv=7;$at=1;}#��ȭ
					
				}
				$bmess.="<br>";
			}else{##��� ����
				$wdmg=int(rand($wat-$edef/2));
				$at=1;
			}
			if($at){
				##ȸ�ǡ�����
				$hitrand=int(rand(2));
				if($eab[12] && 100>int(rand(1200-$efai))){
					$edmg=int(($wdmg+int(rand($estr)))/2);
					if($edmg<1){$edmg=1;}
					$whp-=$edmg;
					if($whp<1){$whp=1;}
					$wdmg=0;
					$hitrand=0;
					$bmess.="<font color=blue size=3>$ename�� ī����!</font><BR>$wname��<font color=red size=3>$edmg</font>�� �������� �־���.";
				}elsif($esh>int(rand(1000))){
					$bmess.="<font color=blue size=3>$ename�� ������� ���� �ְ� �޾Ҵ�.</font>";
					$wdmg=0;
					$hitrand=0;
				}elsif($esh2>int(rand(1000))){
					$bmess.="<font color=blue size=3>$ename�� ���� ��.</font>";
					$wdmg=0;
					$hitrand=0;
				}elsif($wcl>int(rand(1000))){
					$bmess.="<font color=blue size=4>����!</font>";
					$wdmg=int($wdmg*1.5);
					if($wab[23]){
						$wdmg=int($wdmg*$wabdmg[23]);
					}
				}
				##������
				if($wdmg<=0 && $hitrand eq 0){
					$wdmg=0;
					$bmess.="<font color=red>$ename</font>�� �������� �־����� �ʾҴ�.<BR>";
				}elsif($wdmg<=0){
					$wdmg=1;
				}
				if($wdmg){
					$bmess.="<font color=red>$ename</font>��<font color=red size=4>$wdmg</font>�� �������� �־���.<BR>";
					if(int(rand(4)) eq 2) < 1){
						$epara=$wabdmg[14];
						if(!$epara){$epara=1;}
						$bmess.="<font color=red>$ename�� ���� ��������.</font><BR>";
					}
					elsif($wsv eq 4 && $ehit>20){
						$wsh+=40;
						$bmess.="<font color=red>$ename�� �������� ���ȴ�.</font><BR>";
					}
					elsif(int(rand(8)) eq 2 && $wsv eq 5 && $ehit>20){
						$epara2=1;
						$bmess.="<font color=red>$ename�� ����Ǿ���.</font><BR>";
					}
					elsif($wsv eq 6 || $wab[28] && int(rand(4)) eq 1){
						$whpup=int($wdmg/2);
						$whp+=$whpup;
						if($whp>$wmaxhp){$whp=$wmaxhp;}
						$bmess.="$wname�� HP��<font color=blue>$whpup</font>����ߴ�.<BR>";
					}
					elsif(int(rand(8)) eq 2 && $wsv eq 7){
						$espeed-=50;
						if($espeed<0){$espeed=0;}
						$bmess.="<font color=red>$ename�� �������� �ʾ�����.</font><BR>";
					}elsif($wab[26] && int(rand(3)) eq 1){
						$addmg = int(rand(200));
						$bmess.="<font color=red size=2>���� ��<b>$addmg</b>�� �߰� �������� �־���.</font><BR>";
						$wdmg += $addmg;
					}
					elsif($wab[27] && int(rand(3)) eq 1){
						$msmp=int(rand(150));
						$emp-=$msmp;
						if($emp<0){$emp=0;}
						$wmp+=$msmp;
						if($wmp>$wmaxmp){$wmp=$wmaxmp;}
						$bmess.="$ename�� MP��<font color=red>$msmp</font>���ѾҴ�.<BR>";
					}
					elsif($wab[31] && int(rand(2)) eq 1){
						$abrand = int(rand(2));
						$iab = $esk[$abrand];
						$atype = $eabtype[$iab];
						if($eab[$atype]){
							$eab[$atype] = 0;
							$bmess.="<font color=red>$ename�� �����Ƽ :$eabname[$iab]�� ���ߴ�!</font><BR>";
						}
					}
					if(int(rand(30)) eq 7 && $wsv eq 1 || $wab[9] && int(rand(1000)) < $wabdmg[9]){
						$ehp=0;
						$bmess.="<font color=red>$ename�� ����ߴ�.</font><BR>";
					}
				}
					$ehp-=$wdmg;
			}
			if($ehp<=0 && $eab[11]  && int(rand(100)) < $eabdmg[11]){
				$ehp=int($emaxhp/2);
				$bmess.="<font color=red>$ename�� ��Ȱ�ߴ�!</font><BR>";
			}elsif($ehp<=0){
				$ehp=0;
				$win=1;
				$bmess.="$ename�� �Ѿ�߷ȴ�.<BR>";
			}
		
			if($kou>10){&error;}
			if($win){last;}
		}
		$bmess.="<BR>";
	}else{$bmess.="<font color=red>$wname�� ������ �� ����.</font><BR>";}
	$wpara2=0;
}
sub eat{
	if(!$epara2){
		if($eab[1]){
			$hpsai=int($eabdmg[1]/100*$emaxhp);
			$ehp+=$hpsai;
			if($ehp>$emaxhp){$ehp=$emaxhp;}
			$bmess.="[���]$ename�� HP��<font color=blue>$hpsai</font>ȸ���ߴ�.<BR>";
		}
		$ekai = int($espeed/100 + rand($espeed/100)) + 1;
		if($ekai<1){$ekai=1;}
		if($ekai>=8){$ekai=8;}

		$bmess.="<font color=red>$ename</font>��$ekaiȸ����!<BR>";
		if($epara){
			$ehpd=int(rand($emaxhp*$epara/10));
			$ehp-=$ehpd;
			if($ehp<=1){$ehp=1;}
			$bmess.="<font color=red>���� ����$ehpd�� �������� �޾Ҵ�.</font><BR>";
		}
		
		for($kou=0;$kou<$ekai;$kou++){
			$rand=int(rand(100)) ;$at=0;$esv=0;
			if($emp/($emaxmp+1)*100<=$emprate){$magic=1;}
			elsif($ehp/($emaxhp+1)*100<=$ehprate){$magic=2;}
			else{$magic=0;}
			##��� �ߵ�
			$mpdown=$etec_mp[$magic];
			if($eab[6]){$mpdown-=int($etec_mp[$magic]*$eabdmg[6]/100);}

			if($eab[25]){
				$ehitup=1.5;
			}else{
				$ehitup=1;
			}

			if($etec_hit[$magic]*$ehitup>$rand && $mpdown<=$emp){
				$bmess.="<font color=red size=4><b>$etec_name[$magic] </b></font>";
				if($eab[6]){$bmess.="<font color=blue><b>(�Һ� $eabdmg[6]%�氨)</b></font>";}
				$emp-=$mpdown;
				if($etec_sta[$magic] eq 1){
					$ehpup=$etec_str[$magic] + int(rand($efai/2));
					$ehp+=$ehpup;
					if($ehp>$emaxhp){$ehp=$emaxhp;}
					$bmess.="HP��<font color=blue>$ehpup</font>ȸ���ߴ�.<BR>";
				}elsif($etec_sta[$magic] eq 2){
					$ehp+=int($emaxhp/10);
					$emp+=int($emaxmp/10);
					if($ehp>$emaxhp){$ehp=$emaxhp;}
					if($emp>$emaxmp){$emp=$emaxmp;}
					$bmess.="<font color=blue>HP�� MP�� ȸ���ߴ�.</font><BR>";
				}elsif($etec_sta[$magic] eq 3){
					$eat+=int($efai*($etec_str[$magic]/100));
					$bmess.="<font color=blue>���ݷ��� ����ߴ�.</font><BR>";
				}elsif($etec_sta[$magic] eq 4){
					$edef+=int($efai*($etec_str[$magic]/100));
					$bmess.="<font color=blue>�������� ����ߴ�.</font><BR>";
				}elsif($etec_sta[$magic] eq 5){
					$emdef+=int($efai*($etec_str[$magic]/100));
					$bmess.="<font color=blue>���� �������� ����ߴ�.</font><BR>";
				}elsif($etec_sta[$magic] eq 6){
					$edmg=$etec_str[$magic] + int(rand($eint)) -int($wmdef);
					$esv=6;
					$at=1;
				}elsif($etec_sta[$magic] eq 7){
					$esmp=int(rand($wmaxmp)/5);
					$wmp-=$esmp;
					if($wmp<0){$wmp=0;}
					$emp+=$esmp;
					if($emp>$emaxmp){$emp=$emaxmp;}
					$bmess.="$wname�� MP��<font color=red>$esmp</font>���ѾҴ�.<BR>";
				}elsif($etec_sta[$magic] eq 8){
					$whp=int($whp-$whp/$etec_str[$magic]);
					$bmess.="$wname�� ü���� $etec_str[$magic]���� 1 �����ߴ�.<BR>";
				}else{
					$edmg=$etec_str[$magic] + int(rand($eint)) -int($wmdef);
					if($eab[5]){
						$edmg+=int($edmg*$eabdmg[5]/100);
						$bmess.="<font color=blue><b>(������ +$eabdmg[5]%) </b></font>";
					}
					if($wab[7]){
						$edmg-=int($edmg*$wabdmg[7]/100);
						$bmess.="<font color=blue><b>(������-$wabdmg[7]%) </b></font>";
					}
					$at=1;
					if($etec_sta[$magic] eq 9){$esv=1;}#���
					if($etec_sta[$magic] eq 10){$esv=2;}#��� �ٿ�
					if($etec_sta[$magic] eq 11){$esv=3;}#��
					if($etec_sta[$magic] eq 12){$esv=4;}#���� �ٿ�
					if($etec_sta[$magic] eq 13){$esv=5;}#����
					if($etec_sta[$magic] eq 14){$esv=7;}#��ȭ
				}
				$bmess.="<br>";
			}else{##��� ����
				$edmg=int(rand($eat-$wdef/2));
				$at=1;
			}
			if($at){
				##ȸ��, ����
				$hitrand=int(rand(2));
				if($wab[12] && 100>int(rand(1200-$wfai))){
					$wdmg=int(($edmg+int(rand($wstr)))/2);
					if($wdmg<1){$wdmg=1;}
					$ehp-=$wdmg;
					if($ehp<1){$ehp=1;}
					$edmg=0;
					$hitrand=0;
					$bmess.="<font color=blue size=3>$wname�� ī����!</font><BR>$ename��<font color=red size=3>$wdmg</font>�� �������� �־���.";
				}elsif($wsh>int(rand(1000))){
					$bmess.="<font color=blue size=3>$wname�� ������� ���� �ְ� �޾Ҵ�.</font>";
					$edmg=0;
					$hitrand=0;
				}elsif($wsh2>int(rand(1000))){
					$bmess.="<font color=blue size=3>$wname�� ���� ��.</font>";
					$edmg=0;
					$hitrand=0;
				}elsif($ecl>int(rand(1000))){
					$bmess.="<font color=blue size=4>����!</font>";
					$edmg=int($edmg*1.5);
					if($eab[23]){
						$edmg=int($edmg*$eabdmg[23]);
					}
				}
				##������
				if($edmg<=0 && $hitrand eq 0){
					$edmg=0;
					$bmess.="<font color=blue>$wname</font>�� �������� �־����� �ʾҴ�.<BR>";
				}elsif($edmg<=0){
					$edmg=1;
				}
				if($edmg){
					$bmess.="<font color=blue>$wname</font>��<font color=red size=4>$edmg</font>�� �������� �־���.<BR>";
					if($esv eq 2){
						$wdef-=int($wdef/50);
						$bmess.="$wname�� ������ ���ȴ�.<BR>";
					}
					elsif(int(rand(4)) eq 2 && $esv eq 3 || $eab[14] && int(rand(6)) < 1){
						$wpara=$eabdmg[14];
						if(!$wpara){$wpara=1;}
						$bmess.="<font color=red>$wname�� ���� ��������.</font><BR>";
					}
					elsif($esv eq 4 && $whit>20){
						$esh+=40;
						$bmess.="<font color=red>$wname�� �������� ���ȴ�.</font><BR>";
					}
					elsif(int(rand(8)) eq 2 && $esv eq 5){
						$wpara2=1;
						$bmess.="<font color=red>$wname�� ����Ǿ���.</font><BR>";
					}
					elsif($esv eq 6 || $eab[28] && int(rand(4)) eq 1){
						$ehpup=int($edmg/2);
						$ehp+=$ehpup;
						if($ehp>$emaxhp){$ehp=$emaxhp;}
						$bmess.="$ename�� HP��<font color=blue>$ehpup</font>����ߴ�.<BR>";
					}
					elsif(int(rand(8)) eq 2 && $esv eq 7){
						$wspeed-=50;
						if($wspeed<0){$wspeed=0;}
						$bmess.="<font color=red>$wname�� �������� �ʾ�����.</font><BR>";
					}
					elsif($eab[26] && int(rand(3)) eq 1){
						$addmg = int(rand(200));
						$bmess.="���� ��<font color=red size=2><b>$addmg</b></font>�� �߰� �������� �־���.<BR>";
						$edmg += $addmg;
					}
					elsif($eab[27] && int(rand(3)) eq 1){
						$esmp=int(rand(150));
						$wmp-=$esmp;
						if($wmp<0){$wmp=0;}
						$emp+=$esmp;
						if($emp>$emaxmp){$emp=$emaxmp;}
						$bmess.="$wname�� MP��<font color=red>$esmp</font>���ѾҴ�.<BR>";
					}
					elsif(int(rand(30)) eq 7 && $esv eq 1 || $eab[9] && int(rand(1000)) < $eabdmg[9]){
						$whp=0;
						$bmess.="<font color=red>$wname�� ����ߴ�.</font><BR>";
					}
					elsif($eab[31] && int(rand(7)) eq 5){
						$abrand = int(rand(2));
						$iab = $wsk[$abrand];
						$atype = $wabtype[$iab];
						if($wab[$atype]){
							$wab[$atype] = 0;
							$bmess.="<font color=red>$wname�� �����Ƽ :$wabname[$iab]�� ���ߴ�!</font><BR>";
						}
					}
				}
				$whp-=$edmg;
			}
			if($whp<=0 && $wab[11]  && int(rand(100)) < $wabdmg[11]){
				$whp=int($wmaxhp/2);
				$bmess.="<font color=red>$wname�� ��Ȱ�ߴ�!</font><BR>";
			}elsif($whp<=0){
				$whp=0;
				$lose=1;
				$bmess.="<font color=red>$wname�� ���� ���ߴ�.</font><BR>";
			}
			if($kou>10){&error("��ȸ �����ؿ� ����");}
			if($lose){last;}
		}
		$bmess.="<BR>";
	}else{$bmess.="<font color=red>$ename�� ������ �� ����.</font><BR>";}
	$epara2=0;
}

sub gprint{
	$blog.= <<"EOF";
<TABLE border="0" width="100%" align=center height="144" CLASS=TOC>
  <TBODY>
    <TR>
      <TD colspan="3" align="center" bgcolor="$ELE_BG[$town_ele]"><FONT color="#ffffcc">õ�� ���� ����ȸ</FONT></TD>
    </TR>
    <TR>
      <TD bgcolor="#cccccc" width="30%">
      <TABLE border="0" width="100%" height="100%" bgcolor=$ELE_BG[$wele] align=right>
        <TBODY>
          <TR>
            <TD rowspan="2"><FONT size="-1"><img src="./img/chara/$wchara.gif"></FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">HP</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$whp/$wmaxhp</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">���ݷ�</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$wstr $chi1(+$warmdmg)</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">����</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$warmname<BR>
            ��$warmdmg/$warmwei��</FONT></TD>
          </TR>
          <TR>
            <TD bgcolor=$FCOLOR2><FONT size="-1">MP</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$wmp/$wmaxmp</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">����</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$wvit $chi1(+$wprodmg+$waccdmg)</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">��</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$wproname<BR>
            ��$wprodmg/$wprowei��</FONT></TD>
          </TR>
          <TR>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$wname</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">����</FONT></TD>
            <TD bgcolor=$FCOLOR2>$JOB[$wclass]</TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">�ӵ�</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$wagi</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">�Ǽ��縮</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$waccname<BR>
            ��$waccdmg/$waccwei��</FONT></TD>
          </TR>
        </TBODY>
      </TABLE>
      </TD>
      <TD bgcolor="#cccccc" width=30%>
      <TABLE border="0" width="100%" height="100%" bgcolor=$ELE_BG[$eele]>
        <TBODY>
          <TR>
            <TD rowspan="2"><FONT size="-1"><img src="./img/chara/$echara.gif"></FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">HP</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$ehp/$emaxhp</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">���ݷ�</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$estr $chi2(+$earmdmg)</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">����</FONT></TD>
	    <TD bgcolor=$FCOLOR2><FONT size="-1">$earmname<BR>��$earmdmg/$earmwei��</FONT></TD>
          </TR>
          <TR>
            <TD bgcolor=$FCOLOR2><FONT size="-1">MP</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$emp/$emaxmp</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">����</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$evit $chi2(+$eprodmg+$eaccdmg)</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">��</FONT></TD>
	    <TD bgcolor=$FCOLOR2><FONT size="-1">$eproname<BR>��$eprodmg/$eprowei��</FONT></TD>
         </TR>
          <TR>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$ename</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">����</FONT></TD>
            <TD bgcolor=$FCOLOR2>$JOB[$eclass]</TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">�ӵ�</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$eagi</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">�Ǽ��縮</FONT></TD>
	    <TD bgcolor=$FCOLOR2><FONT size="-1">$eaccname<BR>��$eaccdmg/$eaccwei��</FONT></TD>
          </TR>
        </TBODY>
      </TABLE>
      </TD>
    </TR>
    <TR>
      <TD bgcolor=#000000><font color="white" size="-1">��$wcom��</font></TD>
      <TD bgcolor=#000000><font color="white" size="-1">��$ecom��</font></TD>
    </TR>
  </TBODY>
</TABLE>
<BR><BR>
EOF
}
sub bprint{
	$blog.= <<"EOF";
<CENTER>
<TABLE border="0" width="80%" bgcolor="#000000" CLASS=TC>
  <TBODY>
    <TR>
      <TD colspan="8" align="center" bgcolor="$FCOLOR"><B><FONT color="#ffffcc">$turn ��</FONT></B></TD>
    </TR>
    <TR>
      <TD colspan="8" align="center" bgcolor="000000"><B><img src=./img/etc/arena.jpg></B></TD>
    </TR>
    <TR>
      <TD bgcolor="$ELE_C[2]" align="center"><IMG src="./img/chara/$wchara.gif"></TD>
      <TD colspan="6" bgcolor="$FCOLOR2" align="center"><font size=2>$bmess</font></TD>
      <TD bgcolor="$ELE_C[1]" align="center"><IMG src="./img/chara/$echara.gif"></TD>
    </TR>
    <TR>
      <TD bgcolor="$ELE_BG[2]" colspan=4 width=12.5%>$wname</TD>
      <TD bgcolor="$ELE_BG[1]" colspan=4 width=12.5%>$ename</TD>
    </TR><TR>
      <TD bgcolor="$ELE_C[2]" width=12.5%>HP</TD>
      <TD bgcolor="$ELE_C[2]" width=12.5%>$whp/$wmaxhp</TD>
      <TD bgcolor="$ELE_C[2]" width=12.5%>MP</TD>
      <TD bgcolor="$ELE_C[2]" width=12.5%>$wmp/$wmaxmp</TD>
      <TD bgcolor="$ELE_C[1]" width=12.5%>HP</TD>
      <TD bgcolor="$ELE_C[1]" width=12.5%>$ehp/$emaxhp</TD>
      <TD bgcolor="$ELE_C[1]" width=12.5%>MP</TD>
      <TD bgcolor="$ELE_C[1]" width=12.5%>$emp/$emaxmp</TD>
    </TR>
  </TBODY>
</TABLE>
</CENTER>
<BR><BR><BR><P>
EOF
}
sub c_open{
	open(IN,"./logfile/chara/$wid.cgi") or &error2('ĳ���� ������ ������ ���� �ʾҽ��ϴ�.');
	@W_DATA = <IN>;
	close(IN);
	($wid,$wpass,$wname,$wurl,$wchara,$wsex,$whp,$wmaxhp,$wmp,$wmaxmp,$wele,$wstr,$wvit,$wint,$wfai,$wdex,$wagi,$wmax,$wcom,$wgold,$wbank,$wex,$wtotalex,$wabp,$wjp,$wcex,$wunit,$wcon,$warm,$wpro,$wacc,$wtec,$wsta,$wpos,$wmes,$whost,$wdate,$wdate2,$wclass,$wtotal,$wkati,$wtype,$woya,$wsk,$wflg,$wflg2,$wflg3,$wflg4,$wflg5) = split(/<>/,$W_DATA[0]);
	$wlv = int($wex/100)+1;

	open(IN,"./logfile/chara/$eid.cgi") or &error2('ĳ���� ������ ������ ���� �ʾҽ��ϴ�.');
	@E_DATA = <IN>;
	close(IN);
	($eid,$epass,$ename,$eurl,$echara,$esex,$ehp,$emaxhp,$emp,$emaxmp,$eele,$estr,$evit,$eint,$efai,$edex,$eagi,$emax,$ecom,$egold,$ebank,$eex,$etotalex,$eabp,$ejp,$ecex,$eunit,$econ,$earm,$epro,$eacc,$etec,$esta,$epos,$emes,$ehost,$edate,$esyo,$eclass,$etotal,$ekati,$etype,$eoya,$esk,$eflg,$eflg2,$eflg3,$eflg4,$eflg5) = split(/<>/,$E_DATA[0]);
	$elv = int($eex/100)+1;
}
sub para{
	#�����Ƽ ����
	($wsk[0],$wsk[1]) = split(/,/,$wsk);
	($esk[0],$esk[1]) = split(/,/,$esk);
	open(IN,"./data/ability.cgi");
	@ABILITY = <IN>;
	close(IN);

	foreach(@ABILITY){
		($abno,$abname,$abcom,$abdmg,$abrate,$abpoint,$abclass,$abtype) =split(/<>/);
		if($wsk[0] eq $abno || $wsk[1] eq $abno || $warmsta eq $abno || $wprosta eq $abno || $waccsta eq $abno){
			$wab[$abtype]=1;
			$wabdmg[$abtype]=$abdmg;
			$wabname[$abno]=$abname;
			$wabtype[$abno]=$abtype;
		}
		if($esk[0] eq $abno || $esk[1] eq $abno || $earmsta eq $abno || $eprosta eq $abno || $eaccsta eq $abno){
			$eab[$abtype]=1;
			$eabdmg[$abtype]=$abdmg;
			$eabname[$abno]=$abname;
			$eabtype[$abno]=$abtype;
		}
	}
	#���� ȿ��
	if($wab[19]){$tup=$wabdmg[19]/100;}
	if($eab[19]){$etup=$eabdmg[19]/100;}
	if($town_ele eq $wele){$waddstr=int($wstr*(0.1 + $tup)) ;$wadddef=int($wvit*(0.1 + $tup)) ;$chi1="<font color=red>��</font>";}
	if($town_ele eq $eele){$eaddstr=int($estr*(0.1 + $etup)) ;$eadddef=int($evit*(0.1 + $etup)) ;$chi2="<font color=red>��</font>";}

	#������
	if($wab[18]){$warmdmg+=int($wint*$wabdmg[18]/100);}
	if($eab[18]){$earmdmg+=int($eint*$eabdmg[18]/100);}

	#���� ���� ���
	$wat=$wstr + $warmdmg + int($warmwei/5) + $waddstr;
	if($wab[2]){$wat+=int($wabdmg[2]/100*$wat);}#�� ��
	$eat=$estr + $earmdmg + int($earmwei/5) + $eaddstr;
	if($eab[2]){$eat+=int($eabdmg[2]/100*$eat);}#�� ��
	
	if($wab[3]){$eat-=int($wabdmg[2]/100*$eat);}#������ �氨
	if($eab[3]){$wat-=int($eabdmg[2]/100*$wat);}#������ �氨
	
	#���� ��� ���
	$wdef=$wvit + $wprodmg + $waccdmg + $wadddef;
	$edef=$evit + $eprodmg + $eaccdmg + $eadddef;

	#���� ��� ���
	$wmdef=int($wfai/2);
	if(int($wsk/10) eq 4){$wmdef+=int($wsklv) /10*$wmdef;}
	
	$emdef=int($efai/2);

	#���� ���
	#$wcl=$warmcl;
	$wcl=30;
	$wcl+=int($wdex/4);
	$ecl=30;
	$ecl+=int($edex/4);
	if($wab[10]){$wcl+=$wabdmg[10]*10;}
	if($eab[10]){$ecl+=$eabdmg[10]*10;}
	if($wcl>200){$wcl=200;}
	if($ecl>200){$ecl=200;}

	#ȸ���� ���
	$wsh=int($wdex/3);
	$esh=int($edex/3);
	if($wab[8]){$wsh2+=$wabdmg[8]*10;}
	if($eab[8]){$esh2+=$eabdmg[8]*10;}

	#���� ȸ��
	$wadagi=0;
	$eadagi=0;

	if($wab[4]){$wadkai=$wabdmg[4]* 50;}#���� �ľ�
	if($eab[4]){$eadkai=$eabdmg[4]* 50;}#���� �ľ�
		
	$wspeed=$wagi-$warmwei-$wprowei-$waccwei+$wadagi + $wadkai;
	$espeed=$eagi-$earmwei-$eprowei-$eaccwei+$eadagi + $eadkai;
	
	#HP��� 1
	$whp=$wmaxhp;
	$wmp=$wmaxmp;

	#HP��� 2
	$ehp=$emaxhp;
	$emp=$emaxmp;
}
sub t_open{
	open(IN,"./data/tec.cgi") or &error('������ ���� �ʾҽ��ϴ�.');
	@TEC = <IN>;
	close(IN);
	($wtec1,$wtec2,$wtec3,$wmprate,$whprate) =split(/,/,$wtec);
	
	if($wtec1 eq ""){$wtec1=0;}
	if($wtec2 eq ""){$wtec2=0;}
	if($wtec3 eq ""){$wtec3=0;}

	($wtec_name[0],$wtec_str[0],$wtec_hit[0],$wtec_mp[0],$wtec_ab[0],$wtec_sta[0],$wtec_class[0]) = split(/<>/,$TEC[$wtec1]);
	($wtec_name[1],$wtec_str[1],$wtec_hit[1],$wtec_mp[1],$wtec_ab[1],$wtec_sta[1],$wtec_class[1]) = split(/<>/,$TEC[$wtec2]);
	($wtec_name[2],$wtec_str[2],$wtec_hit[2],$wtec_mp[2],$wtec_ab[2],$wtec_sta[2],$wtec_class[2]) = split(/<>/,$TEC[$wtec3]);
	
	
	($etec1,$etec2,$etec3,$emprate,$ehprate) =split(/,/,$etec);
	if($etec1 eq ""){$etec1=0;}
	if($etec2 eq ""){$etec2=0;}
	if($etec3 eq ""){$etec3=0;}

	($etec_name[0],$etec_str[0],$etec_hit[0],$etec_mp[0],$etec_ab[0],$etec_sta[0],$etec_class[0]) = split(/<>/,$TEC[$etec1]);
	($etec_name[1],$etec_str[1],$etec_hit[1],$etec_mp[1],$etec_ab[1],$etec_sta[1],$etec_class[1]) = split(/<>/,$TEC[$etec2]);
	($etec_name[2],$etec_str[2],$etec_hit[2],$etec_mp[2],$etec_ab[2],$etec_sta[2],$etec_class[2]) = split(/<>/,$TEC[$etec3]);
}
sub eq_open{
	($warmno,$warmname,$warmval,$warmdmg,$warmwei,$warmele,$warmhit,$warmcl,$warmsta,$warmtype,$warmflg) = split(/,/,$warm);
	($wprono,$wproname,$wproval,$wprodmg,$wprowei,$wproele,$wprohit,$wprocl,$wprosta,$wprotype,$wproflg) = split(/,/,$wpro);
	($waccno,$waccname,$waccval,$waccdmg,$waccwei,$waccele,$wacchit,$wacccl,$waccsta,$wacctype,$waccflg) = split(/,/,$wacc);
	if($wele eq "$warmele" && $warmele ne "0"){$warmdmg=int($warmdmg*1.2);}
	if($wele eq "$wproele" && $warmele ne "0"){$wprodmg=int($wprodmg*1.2);}
	if($wele eq "$waccele" && $warmele ne "0"){$waccdmg=int($waccdmg*1.5);}
	if($ARM[$wclass] eq "$warmtype"){$warmhit+=10;}
	
	if($eid){
		($earmno,$earmname,$earmval,$earmdmg,$earmwei,$earmele,$earmhit,$earmcl,$earmsta,$earmtype,$earmflg) = split(/,/,$earm);
		($eprono,$eproname,$eproval,$eprodmg,$eprowei,$eproele,$eprohit,$eprocl,$eprosta,$eprotype,$eproflg) = split(/,/,$epro);
		($eaccno,$eaccname,$eaccval,$eaccdmg,$eaccwei,$eaccele,$eacchit,$eacccl,$eaccsta,$eacctype,$eaccflg) = split(/,/,$eacc);
		if($eele eq "$earmele" && $earmele ne "0"){$earmdmg=int($earmdmg*1.2);}
		if($eele eq "$eproele" && $eproele ne "0"){$eprodmg=int($eprodmg*1.2);}
		if($eele eq "$eaccele" && $eaccele ne "0"){$eaccdmg=int($eaccdmg*1.5);}
		if($ARM[$eclass] eq "$earmtype"){$earmhit+=10;}
	}
}
sub log_print{
	$header = <<"EOM";
	<html>
	<head>
	<META HTTP-EQUIV="Content-type" CONTENT="text/html; charset=euc-kr">
	<STYLE type="text/css">
	<!--
A:HOVER{
 color: $ALINK
}
.BC {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width :medium; border-color : $ELE_BG[0] $ELE_BG[0] $ELE_BG[0] $ELE_BG[0];border-style : double double double double;background-color : $ELE_BG[0];color : black;}
.TC {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width :medium; border-color : $FCOLOR $FCOLOR $FCOLOR $FCOLOR;border-style : double double double double;background-color : $FCOLOR;color : black;}
.CC {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width :medium; border-color : $ELE_BG[$con_ele] $ELE_BG[$con_ele] $ELE_BG[$con_ele] $ELE_BG[$con_ele];border-style : double double double double;background-color : $ELE_BG[$con_ele];color : black;}
.CC2 {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width :medium; border-color : $ELE_BG[$con2_ele] $ELE_BG[$con2_ele] $ELE_BG[$con2_ele] $ELE_BG[$con2_ele];border-style : double double double double;background-color : $ELE_BG[$con2_ele];color : black;}
.MC {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width :medium; border-color : $ELE_BG[$wele] $ELE_BG[$wele] $ELE_BG[$wele] $ELE_BG[$wele];border-style : double double double double;background-color : $ELE_BG[$wele];color : black;}
.MFC {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width : $ELE_BG[$con_ele];border-top-color : $ELE_BG[$con_ele];border-right-color : $ELE_BG[$con_ele];border-bottom-color : $ELE_BG[$con_ele];border-left-color : $ELE_BG[$con_ele];border-style : double double double double;background-color : $ELE_C[$con_ele];color : black;}
.FC {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width : $FCOLOR;border-top-color : $FCOLOR;border-right-color : $FCOLOR;border-bottom-color : $FCOLOR;border-left-color : $FCOLOR;border-style : double double double double;background-color : $FCOLOR2;color : black;}
.TOC {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width :medium; border-color : $ELE_BG[$town_ele] $ELE_BG[$town_ele] $ELE_BG[$town_ele] $ELE_BG[$town_ele];border-style : double double double double;background-color : $ELE_BG[$town_ele];color : black;}
.dmg { color: #FF0000; font-size: 10pt }
.clit { color: #0000FF; font-size: 10pt }
-->
	</STYLE>
	<title>$TITLE</title></head>
	<body background=\"$BGIF\" bgcolor=\"$BG\">
EOM

	open(OUT,">./data/battle/$ceno.html");
	print OUT $header;
	print OUT $blog;
	print OUT "</BODY></HTML>";
	close(OUT);
}
1;
