
sub CHEACK_COM{

	require './dataroot/nongup.cgi';
	require './dataroot/sangup.cgi';
	require './dataroot/subidae.cgi';
	require './dataroot/pagae.cgi';
	require './dataroot/yuwon.cgi';
	require './dataroot/haya.cgi';
	require './dataroot/hwagae.cgi';
	require './dataroot/banghwa.cgi';
	require './dataroot/naksuk.cgi';
	require './dataroot/herbo.cgi';
	require './dataroot/choto.cgi';
	require './dataroot/minsim.cgi';
	require './dataroot/jingbyung.cgi';
	require './dataroot/yogeak.cgi';
	require './dataroot/hunryeon.cgi';
	require './dataroot/menghun.cgi';
	require './dataroot/dokrip.cgi';
	require './dataroot/senyang.cgi';
	require './dataroot/genguk.cgi';
	require './dataroot/ilgito.cgi';
	require './dataroot/war.cgi';
	require './dataroot/gerae.cgi';
	require './dataroot/edong.cgi';
	require './dataroot/imgwan.cgi';
	require './dataroot/skill1.cgi';
	require './dataroot/jangbi.cgi';
	require './dataroot/songgum.cgi';
	require './dataroot/bokjang.cgi';
	require './dataroot/milser.cgi';
	require './dataroot/susaek.cgi';
	require './dataroot/jiphap.cgi';
	require './dataroot/balryung.cgi';
	require './dataroot/gisul.cgi';
	require './dataroot/def.cgi';
	require './dataroot/pagyeon.cgi';
	require './dataroot/pagyeon2.cgi';

	if($LOCK){&D_F_LOCK;
		if (!-e $lockfile2) {&ERR2("������ ����� ���� �ʰ� �ֽ��ϴ�.");}
	}
	open(IN,"$TOWN_LIST");
	@TOWN_DATA = <IN>;
	close(IN);

	open(IN,"$UNIT_LIST") or &ERR("������ ������ ������ �ʽ��ϴ�.");
	@UNI_DATA = <IN>;
	close(IN);

	$zc=0;
	foreach(@TOWN_DATA){
		($z2name,$z2con,$z2num,$z2nou,$z2syo)=split(/<>/);
		$town_name[$zc] = "$z2name";
		$town_cou[$zc] = "$z2con";
		$town_get[$z2con] += 1;
		$town_num[$z2con] += $z2num;
		$town_nou[$z2con] += $z2nou;
		$town_syo[$z2con] += $z2syo;
		$zc++;
	}

	foreach(@COU_DATA){
		($x2cid,$x2name,$x2ele,$x2mark,$x2king)=split(/<>/);
		$cou_name[$x2cid] = "$x2name";
		$cou_ele[$x2cid] = "$x2ele";
		$cou_mark[$x2cid] = "$x2mark";
		$cou_king[$x2cid] = "$x2king";
	}

	$w_lock = 0;
	if($w_lock){
		open(LOCK,"> ./lock/sangoku") or &ERR2("Can't open lockfile: $!");
		flock(LOCK, 2)           or &ERR2("Can't flock        : $!");
	}

	$dir="./charalog/main";
	if($mmonth eq "1" || $mmonth eq "7"){
		opendir(dirlist,"$dir");
		while($file = readdir(dirlist)){
			if($file =~ /\.cgi/i){
				if(!open(page,"$dir/$file")){
					&ERR2("���� ���� ����!");
				}
				@page = <page>;
				close(page);
				($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex) = split(/<>/,$page[0]);
				$cou_num[$kcon]++;
				$cex_total[$kcon]+=$kcex;
				push(@CL_DATA,"@page<br>");
			}
		}
		closedir(dirlist);
	}



	opendir(dirlist,"$dir");
	$kup_date=0;
	$thit=0;
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR2("���� ���� ����!");
			}
			@page = <page>;
			close(page);
			($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$kskill,$kpoint,$kct,$klevel,$kexp,$kcodea,$kcodeb,$kqpoint) = split(/<>/,$page[0]);


			if($kdate + $TIME_REMAKE < $date && $mtime > $kdate){
				$thit=1;
				($kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex) = split(/,/,$ksub1);

			if($go_ex > 1699){
			&BONG_DEL;
			&DELETE;
			&MAP_LOG("<img src=$IMG/j7.gif> $kname���� �Ƿΰ� �����Ǿ� ���η� ����Ͽ����ϴ�.");
			}

				if($mmonth > 12){$kbank +=1;}


				foreach(@TOWN_DATA){
				($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7],$zname1,$zname2,$zbong1,$zbong2,$zbong3)=split(/<>/);
				if($kid eq "$zbong1"){
					$goldplus = int($zsyo/2);
					$ssalplus = int($znou/2);
				}
				if($kid eq "$zbong2"){
					$goldplus = int($zsyo/2);
					$ssalplus = int($znou/2);
				}
				if($kid eq "$zbong3"){
					$goldplus = int($zsyo/2);
					$ssalplus = int($znou/2);
				}
				if($kid eq ""){
					$goldplus = 0;
					$ssalplus = 0;
				}
				}


				if($mmonth eq "1"){

	&COUNTRY_DATA_OPEN("$kcon");
	if("$xking" eq "$kid"){
		$adv=1000;
	}elsif("$x0" eq "$kid"){
		$adv=700;
	}elsif("$x1" eq "$kid"){
		$adv=600;
	}elsif("$x2" eq "$kid"){
		$adv=400;
	}elsif("$x3" eq "$kid"){
		$adv=400;
	}elsif("$x4" eq "$kid"){
		$adv=400;
	}elsif("$x5" eq "$kid"){
		$adv=200;
	}elsif("$x6" eq "$kid"){
		$adv=200;
	}elsif("$x7" eq "$kid"){
		$adv=200;
	}elsif($x8 eq "$kid"){
		$adv=200;
	}elsif($x9 eq "$kid"){
		$adv=200;
	}elsif($x10 eq "$kid"){
		$adv=200;
	}elsif($x11 eq "$kid"){
		$adv=200;
	}elsif($x12 eq "$kid"){
		$adv=200;
	}elsif($x13 eq "$kid"){
		$adv=200;
	}elsif($x14 eq "$kid"){
		$adv=200;
	}elsif($x15 eq "$kid"){
		$adv=200;
	}elsif($x16 eq "$kid"){
		$adv=200;
	}elsif($x17 eq "$kid"){
		$adv=600;
	}elsif($x18 eq "$kid"){
		$adv=400;
	}elsif($x19 eq "$kid"){
		$adv=400;
	}elsif($x20 eq "$kid"){
		$adv=400;
	}elsif($x21 eq "$kid"){
		$adv=200;
	}elsif($x22 eq "$kid"){
		$adv=200;
	}elsif($x23 eq "$kid"){
		$adv=200;
	}elsif($x24 eq "$kid"){
		$adv=200;
	}elsif($x25 eq "$kid"){
		$adv=200;
	}elsif($x26 eq "$kid"){
		$adv=200;
	}else{$adv=0;}


					$kbank += 1;
					&SALARY;
					if($cou_num[$kcon] eq "0" || $cou_num[$kcon] eq ""){
						$cou_num[$kcon] = 1;
					}
					$kadd = 0;
					if($cex_total[$kcon] ne 0){
					$kadd  = int(($ksal * $kcex / ($cex_total[$kcon] * 1.2))+$kcex * 1.3)+$adv+$goldplus;
					}

					if($kadd > 1000 + $klevel * 150){$kadd=(1000+$klevel*150)+$adv+$goldplus;}
					$kgold += $kadd;
					$k_ex_fol= $kexp;
					if($k_ex_fol > int(200 * (1+($klevel*0.1)))){
						$love = $k_ex_fol - int(200 * (1+($klevel*0.1)));
						$nadd = int(rand(4));
						if($nadd eq "1"){
							$kstr++;
							$add_m = "����";
						}elsif($nadd eq "2"){
							$kint++;
							$add_m = "����";
						}elsif($nadd eq "3"){
							$kcha++;
							$add_m = "�ŷ�";
						}else{
							$klea++;
							$add_m = "��ַ�";
						}
						$max_sal = 1000+$klevel*150;
						$klevel++;
						$kclass += int(200 * (1+($klevel*0.1)));
						&K_LOG("$mmonth�� : [<font color=red>������</font>] $add_m�� 1����Ʈ �ö����ϴ�.");
						&K_LOG("$mmonth�� : [<font color=red>������</font>] Lv.$klevel�� �Ǿ���! ������ <font color=red> $max_sal </font>�� �þ��!");
						&HISTORY_LOG($kid,"Lv.$klevel�� �Ǿ���!");
						$kexp = $love;
					}
					$kcex = 0;
					&K_LOG("$mmonth�� : �������� <font color=red>$kadd</font>�� ���� ¡���߽��ϴ�. [�����߰�����:$adv] [�����߰�����:$goldplus]");
					}elsif($mmonth eq "7"){
					&SALARY;
					if($cou_num[$kcon] eq "0" || $cou_num[$kcon] eq ""){
						$cou_num[$kcon] = 1;
					}
					$kadd = 0;
					if($cex_total[$kcon] ne 0){
						$kadd  = int(($ksal * $kcex / ($cex_total[$kcon] * 1.2)) + $kcex * 1.3 + $ssalplus);
					}

					if($kadd > 1000 + $klevel * 150){$kadd=1000+$klevel*150+$ssalplus;}
					$krice += $kadd;
					$k_ex_fol = $kexp;
					if($k_ex_fol >= int(200 * (1+($klevel*0.1)))){
						$love = $k_ex_fol - int(200 * (1+($klevel*0.1)));

						$nadd = int(rand(4));
						if($nadd eq "1"){
							$kstr++;
							$add_m = "����";
						}elsif($nadd eq "2"){
							$kint++;
							$add_m = "����";
						}elsif($nadd eq "3"){
							$kcha++;
							$add_m = "�ŷ�";
						}else{
							$klea++;
							$add_m = "��ַ�";
						}
						$klevel++;
						$kclass += int(200 * (1+($klevel*0.1)));
						$max_sal = 1000 + $klevel * 150;
						&K_LOG("$mmonth�� : [<font color=red>������</font>] $add_m�� 1����Ʈ �ö����ϴ�!");
						&K_LOG("$mmonth�� : [<font color=red>������</font>] Lv.$klevel�� �Ǿ���! ������ <font color=red> $max_sal </font>�� �þ��!");
						&HISTORY_LOG($kid,"Lv.$klevel�� �Ǿ���!");
						$kexp = $love;
					}
					$kcex = 0;
					&K_LOG("$mmonth�� : ��Ȯ���� <font color=red>$kadd</font>�� �ķ��� ��Ȯ�߽��ϴ�. [�����߰�����:$ssalplus]");
				}
				open(IN,"./charalog/command/$kid\.cgi");
				@COM_DATA = <IN>;
				close(IN);
				($cid,$cno,$cname,$ctime,$csub,$cnum,$cend) = split(/<>/,$COM_DATA[0]);

				$kdate += $TIME_REMAKE;
				&CHARA_MAIN_INPUT;
				splice(@COM_DATA,0,1);
				push(@COM_DATA,"<><><><><><><>\n");

				open(OUT,">./charalog/command/$kid\.cgi");
				print OUT @COM_DATA;
				close(OUT);



				($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7],$zname1,$zname2,$zbong1,$zbong2,$zbong3)=split(/<>/,$TOWN_DATA[$kpos]);
				if($zcon eq "$kcon" || $cid eq "20" || $cid eq "21" || $cid eq "43" || $cid eq "56" || $cid eq "59" || $cid eq "27" || $cid eq "0" || $cid eq "" || ($kskill =~ /Ec/ && $cid eq "18") || $cid eq "63" || $cid eq "61" || $cid eq "64"){

					$kprodmg = 0;
					if($kbook ne "" && $kbook ne 0){
						open(IN,"$PRO_LIST");
						@PRO_DATA = <IN>;
						close(IN);
						($kproname,$kproval,$kprodmg) = split(/<>/,$PRO_DATA[$kbook]);
					}
					&CHARA_ITEM_OPEN;
					if($cid eq "1"){
						&NONGUP;
					}elsif($cid eq "2"){
						&SANGUP;
					}elsif($cid eq "3"){
						&SUBIDAE;
					}elsif($cid eq "34"){
						&PAGAE;
					}elsif($cid eq "36"){
						&YUWON;
					}elsif($cid eq "40"){
						&HAYA;
					}elsif($cid eq "50"){
						&HWAGAE;
					}elsif($cid eq "51"){
						&NAKSUK;
					}elsif($cid eq "52"){
						&HERBO;
					}elsif($cid eq "38"){
						&BANGHWA;
					}elsif($cid eq "32"){
						&CHOTO;
					}elsif($cid eq "8"){
						&MINSIM;
					}elsif($cid eq "10"){
						&JINGBYUNG;
					}elsif($cid eq "45"){
						&PAGYEON;
					}elsif($cid eq "70"){
						&PAGYEON2;
					}elsif($cid eq "11"){
						&HUNRYEON;
					}elsif($cid eq "31"){
						&MENGHUN;
					}elsif($cid eq "47"){
						&SENYANG;
					}elsif($cid eq "41"){
						&GENGUK;
					}elsif($cid eq "49"){
						&DOKRIP;
					}elsif($cid eq "12"){
						&YOGEAK;
					}elsif($cid eq "63"){
						&ILGITO;
					}elsif($cid eq "18"){
						&WAR;
					}elsif($cid eq "19"){
						&GERAE;
					}elsif($cid eq "20"){
						&EDONG;
					}elsif($cid eq "21"){
						&IMGWAN;
					}elsif($cid eq "56"){
						&SKILL1;
					}elsif($cid eq "22"){
						&JANGBI;
					}elsif($cid eq "59"){
						&SONGGUM;
					}elsif($cid eq "23"){
						&BOKJANG;
					}elsif($cid eq "25"){
						&MILSER;
					}elsif($cid eq "27"){
							$ksub2=0;
							$go_ex += int($kbank/2);
							if($cnum eq "1"){
								$kstr_ex +=2;
								$a_mes = "����";
								&K_LOG("$mmonth�� : $a_mes�� ��ȭ�߽��ϴ�.");
							}elsif($cnum eq "2"){
								$kint_ex +=2;
								$a_mes = "����";
								&K_LOG("$mmonth�� : $a_mes�� ��ȭ�߽��ϴ�.");
							}elsif($cnum eq "3"){
								$klea_ex +=2;
								$a_mes = "��ַ�";
								&K_LOG("$mmonth�� : $a_mes�� ��ȭ�߽��ϴ�.");
							}elsif($cnum eq "4"){
								$kcha_ex +=2;
								$a_mes = "�ŷ�";
								&K_LOG("$mmonth�� : $a_mes�� ��ȭ�߽��ϴ�.");
								}
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
					}elsif($cid eq "61"){


							open(IN,"$QUEST_DATA");
							@QUEST_DATA = <IN>;
							close(IN);

							foreach(@QUEST_DATA){
							($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
								if($kcodea =~ /$qcode/ && $qrate > rand(99)){
									if($qcategory =~ /�޽�/){
										$kqpoint += $qup;
										if($qtalkd eq ""){
										}else{
										&K_LOG("$mmonth�� : $qtalkd");
										}
									}
								}
							}

							$ksub2=0;
							if($go_ex < 0){
							&K_LOG("$mmonth�� : ���� ����� �游�� �����Դϴ�.");
								$go_ex=0;
							}else{
							if($kcodea =~ /D3/){
								$kqpoint += 1;
							}
							&K_LOG("$mmonth�� : �Ƿθ� ���� ȸ���Ͽ����ϴ�.");
							$go_ex -= 150;
							}
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
					}elsif($cid eq "64"){
							$ksub2=0;
							if($go_ex < 0){
							&K_LOG("$mmonth�� : ���� ����� �游�� �����Դϴ�.");
								$go_ex=0;
							}else{
							&K_LOG("$mmonth�� : �޾��Ͽ� �Ƿθ� ���� ȸ���Ͽ����ϴ�.");
							$go_ex -= 300;
							}
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
					}elsif($cid eq "65"){

							open(IN,"$QUEST_DATA");
							@QUEST_DATA = <IN>;
							close(IN);

							foreach(@QUEST_DATA){
							($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
								if($kcodea =~ /$qcode/ && $qrate > rand(99)){
									if($qcategory =~ /����/){
										$kqpoint += $qup;
										if($qtalkd eq ""){
										}else{
										&K_LOG("$mmonth�� : $qtalkd");
										}
									}
								}
							}

							$ksub2=0;
							if($go_ex < 0){
							&K_LOG("$mmonth�� : ���� ����� �游�� �����Դϴ�.");
								$go_ex=0;
							}else{
							&K_LOG("$mmonth�� : �����Ͽ� �Ƿθ� ���� ȸ���Ͽ����ϴ�.");
							$go_ex -= 300;
							$kgold -= 300;
							}
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
					}elsif($cid eq "43"){
						&SUSAEK;
					}elsif($cid eq "100"){
						$kpos = 17;
						&K_LOG("$mmonth�� : ��ȸ������ ���� $town_name[$kpos]������ �����߽��ϴ�.");
					}elsif($cid eq "28"){
						&JIPHAP;
					}elsif($cid eq "54"){
						&BALRYUNG;
					}elsif($cid eq "29"){
						&GISUL;
					}elsif($cid eq "30"){
						&DEF;
					}else{
						$ksub2++;
						if($ksub2 > $DEL_TURN){
							&BONG_DEL;
							&DELETE
							&MAP_LOG("<img src=$IMG/j7.gif> $kname���� ���� �ɷ� ����Ͽ����ϴ�.");
						}
						&K_LOG("$mmonth�� : �ƹ��͵� �������� �ʾҽ��ϴ�.");
					}

				}else{
					&K_LOG("$mmonth�� : �ڱ��� �ƴմϴ�.");
				}


				$krice -= int($ksol/20);
				if($krice < 0){

		open(IN,"$DEF_LIST");
		@DEF_LIST3 = <IN>;
		close(IN);

		@NEW_DEF_LIST3=();
		foreach(@DEF_LIST3){
		($did,$dname,$dtown_id,$dtown_flg,$dcon,$dchara,$dsol,$dsub1_ex,$dtown_battle,$ddef) = split(/<>/);
		if("$kid" ne "$did"){
			push(@NEW_DEF_LIST3,"$_");
			}
		}
		open(OUT,">$DEF_LIST");
		print OUT @NEW_DEF_LIST3;
		close(OUT);


					&K_LOG("$mmonth�� : <font color=red>[Ż��] </font>:���� �������� ������ ������� Ż���߽��ϴ�.");
					$ksol = 0;
					$kgat = 0;
					$krice = 0;
				}

				$uhit=0;
				if($kstr_ex >= int($kstr/10)){
					$kstr++;
					$kstr_ex-=int($kstr/10);
					$uhit=1;
					&K_LOG("$mmonth�� : <font color=red>[���] </font>:$kname�� ������ 1����Ʈ �ö���.");
				}
				if($kint_ex >= 10){
					$kint++;
					$kint_ex-=10;
					$uhit=1;
					&K_LOG("$mmonth�� : <font color=red>[���] </font>:$kname�� ������ 1����Ʈ �ö���.");
				}
				if($klea_ex >= 10){
					$klea++;
					$klea_ex-=10;
					$uhit=1;
					&K_LOG("$mmonth�� : <font color=red>[���] </font>:$kname�� ��ַ��� 1����Ʈ �ö���.");
				}
				if($kcha_ex >= 10){
					$kcha++;
					$kcha_ex-=10;
					$uhit=1;
					&K_LOG("$mmonth�� : <font color=red>[���] </font>:$kname�� �ŷ��� 1����Ʈ �ö���.");
				}
				if($uhit){
					$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
				}

				&CHARA_MAIN_INPUT;

				if($ACT_LOG){
					($qsec,$qmin,$qhour,$qday) = localtime($kdate);
					unshift(@ACT_DATA,"$kname���� $qday�� $qhour�� $qmin�� $qsec�ʿ� �ڽ��� �ൿ�� �����߽��ϴ�.\n");
				}
				$kup_date++;
				if($kup_date > $ENTRY_MAX){last;}
			}
		}
	}
	if($thit){
		foreach(@TOWN_DATA){
			$data .= $_;
		}
		&data_save("./log_file","town_data.cgi","$data");
	}

	closedir(dirlist);
	&D_UNLOCK_FILE;


	@NEW_TRAP_DATA = ();
	$trapmax = @TRAP_DATA;
	for($trapi=0;$trapi<$trapmax;$trapi++){
		($tid,$tname,$ttown_id,$tcon,$ttrap,$tint) = split(/<>/,$TRAP_DATA[$trapi]);
		if( open(IN,"./charalog/main/$tid\.cgi") ){
			@E_DATA = <IN>;
			close(IN);
			($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/,$E_DATA[0]);
			if($tcon == $econ){
				push(@NEW_TRAP_DATA,$TRAP_DATA[$trapi]);
			}
		}
	}
	@TRAP_DATA = ();
	@TRAP_DATA = @NEW_TRAP_DATA;

	open(OUT,">$TRAP_LIST");
	print OUT @TRAP_DATA;
	close(OUT);
}
1;
