
sub WAR{
						$ksub2=0;
						($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7],$zname1,$zname2,$zbong1,$zbong2,$zbong3)=split(/<>/,$TOWN_DATA[$cnum]);
						if($zcon eq $kcon){
							&K_LOG("$mmonth�� : �ڱ����� ���ݹ��� �ʽ��ϴ�.");
						}elsif($ksol < 1){
							&K_LOG("$mmonth�� : ������ �����ϴ�.");
						}elsif($z[0] ne $kpos && $z[1] ne $kpos && $z[2] ne $kpos && $z[3] ne $kpos && $z[4] ne $kpos && $z[5] ne $kpos && $z[6] ne $kpos && $z[7] ne $kpos ){
							&K_LOG("$mmonth�� : $zname���� �����ϰ� ���� �ʽ��ϴ�.");
						}else{


							open(IN,"$COUNTRY_LIST");
							@COU_DATA = <IN>;
							close(IN);
							@NEW_COU_DATA=();
							$zvhit=0;
							foreach(@COU_DATA){
								($xvcid,$xvname,$xvele,$xvmark,$xvking,$xvmes,$xvsub,$xvpri)=split(/<>/);
								if($xvcid eq $zcon){$zvhit=1;last;}
							}
							if($zvhit && $xvmark < $BATTLE_STOP){
								&K_LOG("$mmonth�� : $xvname�����Դ� ���� ���ݹ��� �ʽ��ϴ�. ($xvmark ��)");
							}else{
								&COUNTRY_DATA_OPEN("$kcon");
								if($xmark < $BATTLE_STOP){
									&K_LOG("$mmonth�� : $xname���� ���� ���ݹ��� �ʽ��ϴ�. ($xmark ��)");
								}else{
									open(IN,"$DEF_LIST");
									@DEF_LIST3 = <IN>;
									close(IN);
									$d_hit=0;
									foreach(@DEF_LIST3){
										($mdid,$mdname,$mdtown_id,$mdtown_flg,$mdcon,$mdchara) = split(/<>/);
										if($cnum eq $mdtown_id){
											$d_hit=1;last;
										}
									}
									$katt_add2 = 0;
									$kcex += 20;
									$kexp += 20;
									$kpoint += 6;
									&MAP_LOG("<img src=$IMG/j1.gif> $xname���� $kname�δ�� $zname������ �ĵ�� �����ϴ�!");

									$krice -= int($SOL_RICE[$ksub1_ex]*($ksol/60));
									$erice -= int($SOL_RICE[$esub1_ex]*($esol/60));

									$eid="";
			
					if($d_hit){
					%trap = ();
					$trapmax = @TRAP_DATA;
					for($trapi=0;$trapi<$trapmax;$trapi++){
						($tid,$tname,$ttown_id,$tcon,$ttrap,$tint) = split(/<>/,$TRAP_DATA[$trapi]);
						if( $ttown_id == $cnum ){
							$trap{$trapi} = int(rand(65535));
						}
					}

					$t_hit = 0;
					foreach(sort{$trap{$b}<=>$trap{$a}} keys %trap){
						$ttid = $_;
						$t_hit = 1;
					}
					if($t_hit){
						@trapstr = ("","ȭ��","����","�㺸");
						($eid,$ename,$etown_id,$econ,$etrap,$eint) = split(/<>/,$TRAP_DATA[$ttid]);
						$r = int(rand($kintt));
						$ran = int(rand(2000));
						$r1 = int(rand($kleat));
						if(($r - $eint > 0 || ($ksub1_ex == 20 && $ksol > $ran)) && $ksol > 500){
							&K_LOG2("$kname���� $ename���� $trapstr[$etrap]�� �����߽��ϴ�.");
							&E_LOG2("$kname�Կ� ���� ���� $trapstr[$etrap]�� �������߽��ϴ�.");
							splice(@TRAP_DATA,$ttid,1);
							$t_hit = 0;
						}elsif($kskill =~ /Cb/){
							&K_LOG2("$kname���� Ư�� 'ȸ��'�� ���� $ename���� $trapstr[$etrap]�� ȸ���߽��ϴ�.");
							&E_LOG2("$kname���� Ư�� 'ȸ��'�� ���� $trapstr[$etrap]�� ȸ���ع��Ƚ��ϴ�!");
						}elsif($ksub1_ex eq 5){
							&K_LOG2("$kname���� ������ �űͺ��̱� ������ $ename���� $trapstr[$etrap]�� �����ƽ��ϴ�.");
							&E_LOG2("$kname���� ������ �űͺ��̱� ������ $trapstr[$etrap]�� �����ƽ��ϴ�!");
						}elsif($r1 - $eint > 0 || $ksub1_ex eq 5 || $kskill =~ /Cb/){
							&K_LOG2("$kname���� ������� �ϻ�ж��ϰ� �����Ͽ� $ename���� $trapstr[$etrap]�� ȸ���߽��ϴ�.");
							&E_LOG2("$kname���� ������� �ϻ�ж��ϰ� �����Ͽ� $trapstr[$etrap]�� ȸ���ع��Ƚ��ϴ�!");
						}else{
							if($etrap == 1){
								$tdm = int(($ksol/30)*$eint/15);
								if($ksol < $tdm ){
									$tdm = $ksol;
									$ksol = 0;
									$t_hit = 1;
								}else{
									$ksol -= $tdm;
									$t_hit = 0;
								}
								&K_LOG2("$ename���� $trapstr[$etrap]�� �ߵ�! �������̴� $kname���� ���� <font color=red>$tdm</font>���� ����߽��ϴ�.");
								&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth�� : $ename�� $trapstr[$etrap]�� �ߵ��Ͽ� �������̴� $kname�� ������ ���ظ� ���� �� �ϴ�!</font>");
								&E_LOG2("$ename���� $trapstr[$etrap]�� �ߵ�! �������̴� $kname���� ���� <font color=red>$tdm</font>���� ����߽��ϴ�.");
							}elsif($etrap == 2){
								$tdm = int(($ksol/30)*$eint/6);
								if($ksol < $tdm ){
									$tdm = $ksol;
									$ksol = 0;
									$t_hit = 1;
								}else{
									$ksol -= $tdm;
									$t_hit = 0;
								}
								&K_LOG2("$mmonth�� : $ename���� $trapstr[$etrap]�� �ߵ�! ���� ���������� $kname���� ���� <font color=red>$tdm</font>���� ����߽��ϴ�.");
								&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$ename�� $trapstr[$etrap]�� �ߵ��Ͽ� �������̴� $kname�� ������ ������� �� �ϴ�!</font>");
								&E_LOG2("$mmonth�� : $ename���� $trapstr[$etrap]�� �ߵ�! ���� ���������� $kname���� ���� <font color=red>$tdm</font>���� ����߽��ϴ�.");
							}elsif($etrap == 3){
								$tdm = int(($kgat*$eint)/250);
								if($kgat < $tdm ){
									$kgat = 0
								}else{
									$kgat -= $tdm;
								}
								&K_LOG2("$mmonth�� : $ename���� $trapstr[$etrap]�� �ߵ��Ǿ� $kname���� ������ ȥ���� �������ϴ�!");
								&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$ename�� $trapstr[$etrap]�� �ߵ��Ͽ� �������̴� $kname�� �δ밡 ȥ���� ���� �� �ϴ�!</font>");
								&E_LOG2("$mmonth�� : $ename���� $trapstr[$etrap]�� �ߵ��Ǿ� $kname���� ������ ȥ���� �������ϴ�!");
							}

							splice(@TRAP_DATA,$ttid,1);
							open(IN,"./charalog/main/$eid\.cgi");
							@E_DATA = <IN>;
							close(IN);
							($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/,$E_DATA[0]);
							($estr_ex,$eint_ex,$elea_ex,$echa_ex,$esub1_ex,$esub2_ex,$ebo_ex,$egi_ex,$ech_ex,$egu_ex,$ego_ex,$ejin_ex) = split(/,/,$esub1);
							$ecex += 20;
							$eexp += 20;
							&ENEMY_INPUT;


						}
							}
									open(IN,"./charalog/main/$mdid\.cgi");
									@E_DATA = <IN>;
									close(IN);
									($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/,$E_DATA[0]);
									($estr_ex,$eint_ex,$elea_ex,$echa_ex,$esub1_ex,$esub2_ex,$ebo_ex,$egi_ex,$ech_ex,$egu_ex,$ego_ex,$ejin_ex) = split(/,/,$esub1);


									$last_battle=0;
									}else{
										&K_LOG2("���� : $kname�屺��! $zname���� ����밡 ���� �غ��ϰ� �ֽ��ϴ�! ������ �����ϰڽ��ϴ�! [���:$zdef_att]");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth�� : $zname���� ����밡 ���� �غ��ϰ� �ִ� �� �ϴ�! $kname�� �δ�� ������ ������ �¼���!</font>");
										$ename = "$zname��";
										$esol = $zshiro;
										$estrt = int($zdef_att/10);
										$egat = $zpri;
										$last_battle=1;
										$esub1_ex="14";
									}

									if($kcodea =~ /C9/ && 20 > rand(100) && $earm == 16){
										$kqpoint = 1;
										&K_LOG("$mmonth�� : ������ �Ű��� ������ �Լ��Ͽ���.");
									}
									if($ecodea =~ /C9/ && 20 > rand(100) && $karm == 16){
										$eqpoint = 1;
										&E_LOG("$mmonth�� : ������ �Ű��� ������ �Լ��Ͽ���.");
									}

									&K_LOG2("$mmonth�� : $xname���� $kname�δ�� $zname���� �ĵ����ϴ�!");
									&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth�� : $xname���� $kname�δ�� $zname���� �ĵ����ϴ�!</font>");
									&E_LOG2("$mmonth�� : $xname���� $kname�δ�� $zname���� $ename�δ�� ������ �������ϴ�!");

									&CHARA_ITEM_OPEN;


									if($ksub1_ex eq 11){
									$hwarang = int(rand(3));
									if($hwarang eq 0){
										$hwarang1 = $kstrt;
									}elsif($hwarang eq 1){
										$hwarang1 = $kintt;
									}elsif($hwarang eq 2){
										$hwarang1 = $kleat;
									}else{
										$hwarang1 = $kchat;
									}
									}


									if($esub1_ex eq 11){
									$ehwarang = int(rand(3));
									if($ehwarang eq 0){
										$ehwarang1 = $estrt;
									}elsif($ehwarang eq 1){
										$ehwarang1 = $eintt;
									}elsif($ehwarang eq 2){
										$ehwarang1 = $eleat;
									}else{
										$ehwarang1 = $echat;
									}
									}

									if($last_battle eq "1"){
									if($kskill =~ /Eb/){
									$SOL_ATT[0]=20;
									$SOL_ATT[1]=50;
									$SOL_ATT[2]=30;
									$SOL_ATT[3]=50;
									}else{
									$SOL_ATT[1]=30;
									$SOL_ATT[2]=10;
									$SOL_ATT[3]=30;
									}
									$SOL_ATT[5]=$kintt;
									$SOL_ATT[6]=45;
									$SOL_ATT[7]=$kchat;
									$SOL_ATT[8]=75;
									$SOL_ATT[9]=30;
									$SOL_ATT[10]=30;
									$SOL_ATT[11]=$hwarang1;
									if($kskill =~ /Cc/){
									$SOL_ATT[12]=150+$kintt;
									}else{
									$SOL_ATT[12]=150;
									}
									$SOL_ATT[13]=$kchat;
									$SOL_ATT[15]=int($kstrt/2);
									$SOL_ATT[17]=75;
									$SOL_ATT[18]=15;
									$SOL_ATT[19]=30;
									$SOL_ATT[20]=45;
									}else{
									if($kskill =~ /Eb/){
									$SOL_ATT[0]=20;
									$SOL_ATT[1]=50;
									$SOL_ATT[2]=35;
									$SOL_ATT[3]=50;
									}else{
									$SOL_ATT[1]=30;
									$SOL_ATT[2]=15;
									$SOL_ATT[3]=30;
									}
									$SOL_ATT[4]=60;
									$SOL_ATT[5]=$kintt;
									$SOL_ATT[6]=20;
									$SOL_ATT[7]=$kintt+$kchat;
									$SOL_ATT[8]=90;
									$SOL_ATT[9]=45;
									$SOL_ATT[10]=75;
									$SOL_ATT[11]=$hwarang1;
									$SOL_ATT[13]=$kchat;
									$SOL_ATT[15]=$kstrt;
									$SOL_ATT[18]=$kleat;
									$SOL_ATT[19]=60;
									$SOL_ATT[20]=30;
									}

									if($ksub1_ex == 12){
									$SOL_DEF[14] = int($zdef_att/16);
									}else{
									$SOL_DEF[14] = int($zdef_att/8);
									}

									if($eskill =~ /Eb/){
									$SOL_DEF[0]=20;
									$SOL_DEF[1]=20;
									$SOL_DEF[2]=65;
									$SOL_DEF[3]=50;
									}else{
									$SOL_DEF[2]=45;
									$SOL_DEF[3]=30;
									}
									$SOL_DEF[4]=15;
									$SOL_DEF[5]=15;
									$SOL_DEF[6]=$eleat;
									$SOL_DEF[7]=$estrt+$echat;
									$SOL_DEF[8]=90;
									$SOL_DEF[9]=45;
									$SOL_DEF[10]=60;
									$SOL_DEF[11]=$ehwarang1;
									if($eskill =~ /Fb/){
									$SOL_DEF[13]=$echat;
									}else{
									$SOL_DEF[13]=15;
									}
									$SOL_DEF[15]=15;
									$SOL_DEF[16]=$zpri;
									$SOL_DEF[19]=45;
									$SOL_DEF[20]=30;





									if($zname2 == 1){
									$jih = "����";
									$SOL_TYPE1[0] = "100";
									$SOL_TYPE1[1] = "95";
									$SOL_TYPE1[2] = "90";
									$SOL_TYPE1[3] = "100";
									$SOL_TYPE1[4] = "130";
									$SOL_TYPE1[5] = "100";
									$SOL_TYPE1[6] = "80";
									$SOL_TYPE1[7] = "90";
									$SOL_TYPE1[8] = "120";
									$SOL_TYPE1[9] = "80";
									$SOL_TYPE1[10] = "130";
									$SOL_TYPE1[11] = "90";
									$SOL_TYPE1[12] = "100";
									$SOL_TYPE1[13] = "110";
									$SOL_TYPE1[14] = "100";
									$SOL_TYPE1[15] = "90";
									$SOL_TYPE1[16] = "100";
									$SOL_TYPE1[17] = "100";
									$SOL_TYPE1[18] = "100";
									$SOL_TYPE1[19] = "80";
									$SOL_TYPE1[20] = "100";
									}elsif($zname2 == 2){
									$jih = "����";
									$SOL_TYPE1[0] = "100";
									$SOL_TYPE1[1] = "100";
									$SOL_TYPE1[2] = "100";
									$SOL_TYPE1[3] = "120";
									$SOL_TYPE1[4] = "90";
									$SOL_TYPE1[5] = "110";
									$SOL_TYPE1[6] = "110";
									$SOL_TYPE1[7] = "100";
									$SOL_TYPE1[8] = "80";
									$SOL_TYPE1[9] = "80";
									$SOL_TYPE1[10] = "70";
									$SOL_TYPE1[11] = "90";
									$SOL_TYPE1[12] = "100";
									$SOL_TYPE1[13] = "100";
									$SOL_TYPE1[14] = "100";
									$SOL_TYPE1[15] = "100";
									$SOL_TYPE1[16] = "90";
									$SOL_TYPE1[17] = "100";
									$SOL_TYPE1[18] = "80";
									$SOL_TYPE1[19] = "130";
									$SOL_TYPE1[20] = "110";
									}elsif($zname2 == 3){
									$jih = "���";
									$SOL_TYPE1[0] = "100";
									$SOL_TYPE1[1] = "115";
									$SOL_TYPE1[2] = "120";
									$SOL_TYPE1[3] = "100";
									$SOL_TYPE1[4] = "70";
									$SOL_TYPE1[5] = "90";
									$SOL_TYPE1[6] = "100";
									$SOL_TYPE1[7] = "100";
									$SOL_TYPE1[8] = "70";
									$SOL_TYPE1[9] = "130";
									$SOL_TYPE1[10] = "60";
									$SOL_TYPE1[11] = "100";
									$SOL_TYPE1[12] = "100";
									$SOL_TYPE1[13] = "80";
									$SOL_TYPE1[14] = "100";
									$SOL_TYPE1[15] = "110";
									$SOL_TYPE1[16] = "100";
									$SOL_TYPE1[17] = "100";
									$SOL_TYPE1[18] = "110";
									$SOL_TYPE1[19] = "80";
									$SOL_TYPE1[20] = "90";
									}

									if($kskill =~ /Fc/){
									$katt = ($kstrt+$kcha+$SOL_ATT[$ksub1_ex])-int($egat/2);
									}else{
									$katt = ($kstrt+$SOL_ATT[$ksub1_ex])-int($egat/2);
									}

									if($eskill =~ /Fc/){
									$eatt = ($estrt+$echa+$SOL_DEF[$esub1_ex])-int($kgat/2);
									}else{
									$eatt = ($estrt+$SOL_DEF[$esub1_ex])-int($kgat/2);
									}



									if($ksub1_ex == 17){
										if($katt*2 < $eatt){
										$katt = $eatt;
										}
									}
										






									if($ksub1_ex == 0 || $ksub1_ex == 1 || $ksub1_ex == 3 || $ksub1_ex == 9 || $ksub1_ex == 13 || $ksub1_ex == 19 || $ksub1_ex == 20){
										$ksuk = int($bo_ex/3);
										if($ksol >= 500 && $kgat >= 50){
										$bo_ex++;
										}
									}elsif($ksub1_ex == 4 || $ksub1_ex == 8 || $ksub1_ex == 10 || $ksub1_ex == 11){
										$ksuk = int($gi_ex/3);
										if($ksol >= 500 && $kgat >= 50){
										$gi_ex++;
										}
									}elsif($ksub1_ex == 2 || $ksub1_ex == 16 || $ksub1_ex == 15 || $ksub1_ex == 6 || $ksub1_ex == 18){
										$ksuk = int($ch_ex/3);
										if($ksol >= 500 && $kgat >= 50){
										$ch_ex++;
										}
									}elsif($ksub1_ex == 5 || $ksub1_ex == 7 || $ksub1_ex == 12 || $ksub1_ex == 17){
										$ksuk = int($gu_ex/3);
										if($ksol >= 500 && $kgat >= 50){
										$gu_ex++;
										}
									}


									if($esub1_ex == 0 || $esub1_ex == 1 || $esub1_ex == 3 || $esub1_ex == 9 || $esub1_ex == 13 || $esub1_ex == 19 || $esub1_ex == 20){
										$esuk = int($ebo_ex/3);
										if($esol >= 500 && $egat >= 50){
										$ebo_ex++;
										}
									}elsif($esub1_ex == 4 || $esub1_ex == 8 || $esub1_ex == 10 || $esub1_ex == 11){
										$esuk = int($egi_ex/3);
										if($esol >= 500 && $egat >= 50){
										$egi_ex++;
										}
									}elsif($esub1_ex == 2 || $esub1_ex == 16 || $esub1_ex == 15 || $esub1_ex == 6 || $esub1_ex == 18){
										$esuk = int($ech_ex/3);
										if($esol >= 500 && $egat >= 50){
										$ech_ex++;
										}
									}elsif($esub1_ex == 5 || $esub1_ex == 7 || $esub1_ex == 12 || $esub1_ex == 17){
										$esuk = int($egu_ex/3);
										if($esol >= 500 && $egat >= 50){
										$egu_ex++;
										}
									}
									$esub1 = "$estr_ex,$eint_ex,$elea_ex,$echa_ex,$esub1_ex,$esub2_ex,$ebo_ex,$egi_ex,$ech_ex,$egu_ex,$ego_ex,$ejin_ex,";

									if($katt < 0){$katt = 0;}
									if($katt < 0){$kgat = 0;}
									$kex_add=0;
									$eex_add=0;
									if($eatt < 0){$eatt = 0;}
									if($eatt < 0){$egat = 0;}
									$win=0;
									$skill=0;

									if($last_battle eq "0"){
										&K_LOG2("���� : $zname�����κ��� $ename�� $SOL_TYPE[$esub1_ex]�δ밡 ����� �ؿԽ��ϴ�!");
										&K_LOG2("$cou_name[$econ]������ : <$ename> <���� $estrt> <���� $SOL_TYPE[$esub1_ex]> <�Ʒ� $egat> <���� $esol> <���� $jih> <�ش纴������:Lv.$esuk>");
										&K_LOG2("�����ºм� : ���Ʊ������� $katt ������ $SOL_TYPE1[$ksub1_ex]\%�� VS ������������ $eatt ������ $SOL_TYPE1[$esub1_ex]\%��");
										&E_LOG2("���� : $kname�� $SOL_TYPE[$ksub1_ex]�δ밡 $zname�� ������ �����ؿԽ��ϴ�! ����� �غ��ϰڽ��ϴ�!");
										&E_LOG2("$cou_name[$econ]������ : <$kname> <���� $kstrt> <���� $SOL_TYPE[$ksub1_ex]> <�Ʒ� $kgat> <���� $ksol> <���� $jih> <�ش纴������:Lv.$ksuk>");
										&E_LOG2("�����ºм� : ���Ʊ������� $eatt ������ $SOL_TYPE1[$esub1_ex]\%�� VS ������������ $katt ������ $SOL_TYPE1[$ksub1_ex]\%��");
										&BATTLE_LOG("<table border=1 width=274 align=center><tr><td width=100 bgcolor=$ELE_C[$cou_ele[$kcon]]><p align=center><img src=$IMG/$kchara\.gif></p></td><td width=52 height=171 rowspan=3 bgcolor=black><p align=center><b><font color=white>VS</font></b></p></td><td width=100 bgcolor=$ELE_C[$cou_ele[$econ]]><p align=center><img src=$IMG/$echara\.gif></p></td></tr><tr><td width=100 height=19 bgcolor=$ELE_C[$cou_ele[$kcon]]><p align=center><b>$kname<br></b></td><td width=100 height=19 bgcolor=$ELE_C[$cou_ele[$econ]]><p align=center><b>$ename</b></td></tr><tr><td width=100 height=102 bgcolor=black><p><b>��������:$katt</b><br>����:$SOL_TYPE[$ksub1_ex]<br>�Ʒõ�:$kgat<br>������:$SOL_TYPE1[$ksub1_ex]</td><td width=100 height=102  bgcolor=black><b>��������:$eatt</b><br>����:$SOL_TYPE[$esub1_ex]<br>�Ʒõ�:$egat<br>������:$SOL_TYPE1[$esub1_ex]</td></tr></table>");



										$kche = 100;
										$eche = 100;
										$ilrand = int(rand(6));

								

										if($ilrand == 1){
										&K_LOG4("\[$old_date\]$ename(����:$estrt ���:$eleat)�԰� �ϱ��並 ����!");
										&E_LOG4("\[$old_date\]$kname(����:$kstrt ���:$kleat)�԰� �ϱ��並 ����!");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth�� : �͹߳����� ���忡�� �籺�� ���Ѻ��� ��� �ϱ��� ����!</font>");

										if($kskill =~ /Gc/ && rand(100) < 50){
										&K_LOG4("<font color=red>1</font>��:$kname�� �ϼ� �ߵ�! $ename���� ���°� �Ǿ����ϴ�.");
										&E_LOG4("<font color=red>1</font>��:$kname�� �ϼ� �ߵ�! $ename���� ���°� �Ǿ����ϴ�.");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth�� : $kname�� �ϼ��� �ߵ�! $ename�� ���°� �̻��ϴ�!</font>");
										$ego_ex += $kstrt*10;
										if($eqo_ex > 1800){
											$ego_ex = 1800;
										}
										$kpoint += int($kstrt/10);
										&ENEMY_INPUT;
										}else{
										for($count=1;$count<60;$count++){


										if($kche <= 0){last;}

										$kdmge = int((($kstrt+$kleat)/50)+rand(($kstrt+$kleat)/10));
										$edmge = int((($estrt+$eleat)/50)+rand(($estrt+$eleat)/10));

										if($kdmge < 1){
											$kdmge=1;	
										}

							

										$eche -= $kdmge;

										if($eche <= 0){
											&K_LOG4("<font color=red>$count</font>��:$kname�� ü�� $kche (-$edmge\) VS $ename�� ü�� $eche (-$kdmge\)");
											&E_LOG4("<font color=red>$count</font>��:$kname�� ü�� $kche (-$edmge\) VS $ename�� ü�� $eche (-$kdmge\)");
											$wine = 1;
										last;
										}
										
										if($edmge < 1){
											$edmge=1;	
										}

										$kche -= $edmge;

										if($kche <= 0){
											&K_LOG4("<font color=red>$count</font>��:$kname�� ü�� $kche (-$edmge\) VS $ename�� ü�� $eche (-$kdmge\)");
											&E_LOG4("<font color=red>$count</font>��:$kname�� ü�� $kche (-$edmge\) VS $ename�� ü�� $eche (-$kdmge\)");
											last;
										}
										&K_LOG4("<font color=red>$count</font>��:$kname�� ü�� $kche (-$edmge\) VS $ename�� ü�� $eche (-$kdmge\)");
										}
										}

										if($wine){
										$ilgito = int(rand(5));
										if($ilgito == 0){
										$edmg = int($edmg*0.8);
										&K_LOG4("$ename���� ������� ��ȭ�Ǿ����ϴ�.");
										&E_LOG4("$ename���� ������� ��ȭ�Ǿ����ϴ�.");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth�� : �ϱ��� ���, $ename�� �й谡 Ȯ�ǽ�! ������� ��ȭ!</font>");
										}elsif($ilgito == 1){
										if($egold < 1000){
										&K_LOG4("Ż���Ϸ��� ������ $ename���� ���� 1000�̸��Դϴ�.");
										&E_LOG4("Ż����һ������� $ename���� ���� 1000�̸��Դϴ�.");
										}else{
										$goldt = int(rand(1000));
										$kgold += $goldt;
										$egold -= $goldt;
										&K_LOG4("$ename�Կ��Լ� �� $goldt�� Ż���Ͽ����ϴ�.");
										&E_LOG4("$kname�Կ��� �� $goldt�� Ż����߽��ϴ�.");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth�� : �ϱ��� ���, $ename�� �й谡 Ȯ�ǽ�! �� $goldt�� Ż����ߴ�!</font>");
										}
										}elsif($ilgito == 2){
										$ego_ex += rand(100);
										&K_LOG4("$ename�Կ��� �λ��� �������ϴ�!");
										&E_LOG4("$kname�Կ��� �λ��� ���߽��ϴ�!");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth�� : �ϱ��� ���, $ename�� �й谡 Ȯ�ǽ�! �λ��� �Ծ���!</font>");
										}else{
										&K_LOG4("�ϱ���� ���� �ƹ� ���� �������ϴ�.");
										&E_LOG4("�ϱ���� ���� �ƹ� ���� �������ϴ�.");
										}

										&MAP_LOG("<img src=$IMG/j25.gif> $kname���� $ename���� ���� �ϱ��信�� �¸�!");
										&K_LOG4("\[$old_date\]$kname���� $ename���� ���� �ϱ��信�� �¸�!");
										&E_LOG4("\[$old_date\]$kname���� $ename���� ���� �ϱ��信�� �¸�!");
										}else{

										$ilgito = int(rand(5));
										if($ilgito == 0){
										$kdmg = int($kdmg*0.8);
										&K_LOG4("$kname���� ���ݷ��� ��ȭ�Ǿ����ϴ�.");
										&E_LOG4("$kname���� ���ݷ��� ��ȭ�Ǿ����ϴ�.");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth�� : �ϱ��� ���, $kname�� �й谡 Ȯ�ǽ�! ������� ��ȭ!</font>");
										}elsif($ilgito == 1){
										if($kgold < 1000){
										&E_LOG4("Ż���Ϸ��� ������ $kname���� ���� 1000�̸��Դϴ�.");
										&K_LOG4("Ż����һ������� $kname���� ���� 1000�̸��Դϴ�.");
										}else{
										$goldt = int(rand(1000));
										$egold += $goldt;
										$kgold -= $goldt;
										&K_LOG4("$ename�Կ��� �� $goldt�� Ż����߽��ϴ�.");
										&E_LOG4("$kname�Կ��Լ� �� $goldt�� Ż���Ͽ����ϴ�.");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth�� : �ϱ��� ���, $kname�� �й谡 Ȯ�ǽ�! �� $goldt�� Ż�����!</font>");
										}
										}elsif($ilgito == 2){
										$go_ex += rand(100);
										&E_LOG4("$kname�Կ��� �λ��� �������ϴ�!");
										&K_LOG4("$ename�Կ��� �λ��� ���߽��ϴ�!");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth�� : �ϱ��� ���, $kname�� �й谡 Ȯ�ǽ�! �λ��� �Ծ���!</font>");
										}else{
										&K_LOG4("�ϱ���� ���� �ƹ� ���� �������ϴ�.");
										&E_LOG4("�ϱ���� ���� �ƹ� ���� �������ϴ�.");
										}

										&MAP_LOG("<img src=$IMG/j25.gif> $ename���� $kname���� ���� �ϱ��信�� �¸�!");
										&K_LOG4("\[$old_date\]$ename���� $kname���� ���� �ϱ��信�� �¸�!");
										&E_LOG4("\[$old_date\]$ename���� $kname���� ���� �ϱ��信�� �¸�!");
										}

										}elsif($ilrand == 2){
										&K_LOG4("\[$old_date\]$ename(����:$eintt �ŷ�:$echat)�԰� ������ ����!");
										&E_LOG4("\[$old_date\]$kname(����:$kintt �ŷ�:$kchat)�԰� ������ ����!");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth�� : ���� �������� ������� ���� ȣ���� ġ�� �����ߴ�!</font>");
										for($count=1;$count<60;$count++){

										if($kche <= 0){last;}

										$kdmge = int((($kintt+$kchat)/50)+rand(($kintt+$kchat)/10));
										$edmge = int((($eintt+$echat)/50)+rand(($eintt+$echat)/10));

										if($kdmge < 1){
											$kdmge=1;	
										}

							

										$eche -= $kdmge;

										if($eche <= 0){
											$eche = 0;
											&K_LOG4("<font color=red>$count</font>ȸ:$kname�� ���ŷ� $kche (-$edmge\) VS $ename�� ���ŷ� $eche (-$kdmge\)");
											&E_LOG4("<font color=red>$count</font>ȸ:$kname�� ���ŷ� $kche (-$edmge\) VS $ename�� ���ŷ� $eche (-$kdmge\)");
											$wine = 1;
										last;
										}
										
										if($edmge < 1){
											$edmge=1;	
										}

										$kche -= $edmge;

										if($kche <= 0){
											$kche = 0;
											&K_LOG4("<font color=red>$count</font>ȸ:$kname�� ���ŷ� $kche (-$edmge\) VS $ename�� ���ŷ� $eche (-$kdmge\)");
											&E_LOG4("<font color=red>$count</font>ȸ:$kname�� ���ŷ� $kche (-$edmge\) VS $ename�� ���ŷ� $eche (-$kdmge\)");
											last;
										}
										&K_LOG4("<font color=red>$count</font>ȸ:$kname�� ���ŷ� $kche (-$edmge\) VS $ename�� ���ŷ� $eche (-$kdmge\)");
										}

										if($wine){
										$ilgito = int(rand(5));
										if($ilgito == 0){
										$edmg = int($edmg*0.8);
										&K_LOG4("$ename���� ������� ��ȭ�Ǿ����ϴ�.");
										&E_LOG4("$ename���� ������� ��ȭ�Ǿ����ϴ�.");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth�� : ���� ���, $ename�� �й谡 Ȯ�ǽ�! ������� ��ȭ!</font>");
										}elsif($ilgito == 1){
										if($egold < 1000){
										&K_LOG4("Ż���Ϸ��� ������ $ename���� ���� 1000�̸��Դϴ�.");
										&E_LOG4("Ż����һ������� $ename���� ���� 1000�̸��Դϴ�.");
										}else{
										$goldt = int(rand(1000));
										$kgold += $goldt;
										$egold -= $goldt;
										&K_LOG4("$ename�Կ��Լ� �� $goldt�� Ż���Ͽ����ϴ�.");
										&E_LOG4("$kname�Կ��� �� $goldt�� Ż����߽��ϴ�.");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth�� : ���� ���, $ename�� �й谡 Ȯ�ǽ�! �� $goldt�� Ż�����!</font>");
										}
										}elsif($ilgito == 2){
										$ego_ex += rand(100);
										&K_LOG4("$ename�Կ��� �λ��� �������ϴ�!");
										&E_LOG4("$kname�Կ��� �λ��� ���߽��ϴ�!");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth�� : ���� ���, $ename�� �й谡 Ȯ�ǽ�! �λ��� ����!</font>");
										}else{
										&K_LOG4("�������� ���� �ƹ� ���� �������ϴ�.");
										&E_LOG4("�������� ���� �ƹ� ���� �������ϴ�.");
										}

										&MAP_LOG("<img src=$IMG/j26.gif> $kname���� $ename���� ���� �������� �¸�!");
										&K_LOG4("\[$old_date\]$kname���� $ename���� ���� �������� �¸�!");
										&E_LOG4("\[$old_date\]$kname���� $ename���� ���� �������� �¸�!");
										}elsif(!$wine){
										$ilgito = int(rand(5));
										if($ilgito == 0){
										$kdmg = int($kdmg*0.8);
										&K_LOG4("$kname���� ���ݷ��� ��ȭ�Ǿ����ϴ�.");
										&E_LOG4("$kname���� ���ݷ��� ��ȭ�Ǿ����ϴ�.");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth�� : ���� ���, $kname�� �й谡 Ȯ�ǽ�! ���ݷ��� ��ȭ!</font>");
										}elsif($ilgito == 1){
										if($kgold < 1000){
										&E_LOG4("Ż���Ϸ��� ������ $kname���� ���� 1000�̸��Դϴ�.");
										&K_LOG4("Ż����һ������� $kname���� ���� 1000�̸��Դϴ�.");
										}else{
										$goldt = int(rand(1000));
										$egold += $goldt;
										$kgold -= $goldt;
										&K_LOG4("$ename�Կ��� �� $goldt�� Ż����߽��ϴ�.");
										&E_LOG4("$kname�Կ��Լ� �� $goldt�� Ż���Ͽ����ϴ�.");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth�� : ���� ���, $kname�� �й谡 Ȯ�ǽ�! �� $goldt�� Ż�����!</font>");
										}
										}elsif($ilgito == 2){
										$go_ex += rand(100);
										&E_LOG4("$kname�Կ��� �λ��� �������ϴ�!");
										&K_LOG4("$ename�Կ��� �λ��� ���߽��ϴ�!");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth�� : ���� ���, $kname�� �й谡 Ȯ�ǽ�! �λ��� ����!</font>");
										}else{
										&K_LOG4("�������� ���� �ƹ� ���� �������ϴ�.");
										&E_LOG4("�������� ���� �ƹ� ���� �������ϴ�.");
										}
										&MAP_LOG("<img src=$IMG/j26.gif> $ename���� $kname���� ���� �������� �¸�!");
										&K_LOG4("\[$old_date\]$ename���� $kname���� ���� �������� �¸�!");
										&E_LOG4("\[$old_date\]$ename���� $kname���� ���� �������� �¸�!");
										}
										}

									}


										open(IN,"./charalog/command1/$kid\.cgi");
										@KCOM = <IN>;
										close(IN);

										open(IN,"./charalog/command1/$eid\.cgi");
										@ECOM = <IN>;
										close(IN);
									

										$W_JEN_SUL[1] = 10;
										$W_JEN_SUL[2] = 10;
										$W_JEN_SUL[3] = 10;
										$W_JEN_SUL[4] = 15;
										$W_JEN_SUL[5] = 15;
										$W_JEN_SUL[6] = 15;
										$W_JEN_SUL[11] = 28;
										$W_JEN_SUL[12] = 18;
										$W_JEN_SUL[13] = 22;
										$W_JEN_SUL[14] = 20;
										$W_JEN_SUL[15] = 15;
										$W_JEN_SUL[16] = 15;
										$W_JEN_SUL[18] = 40;

										$L_JEN_SUL[1] = -10;
										$L_JEN_SUL[2] = -10;
										$L_JEN_SUL[3] = -10;
										$L_JEN_SUL[4] = -12;
										$L_JEN_SUL[5] = -12;
										$L_JEN_SUL[6] = -12;
										$L_JEN_SUL[11] = -15;
										$L_JEN_SUL[12] = -12;
										$L_JEN_SUL[13] = -15;
										$L_JEN_SUL[14] = -12;
										$L_JEN_SUL[15] = -12;
										$L_JEN_SUL[16] = -8;
										$L_JEN_SUL[18] = -25;


										$gg = 0;
										for($count=0;$count<30;$count++){
										$gg++;
				
										if(($karm != 17 && $kcno == 11) || ($ksub1_ex != 5 && $kcno == 14) || ($ksub1_ex != 7 && $kcno == 16) || ($ksub1_ex != 11 && $kcno == 15) || ($karm != 18 && $kcno == 12) || ($karm != 19 && $kcno == 13)){
											$kcno = 0;
											$kccp = 0;
											$krap = 0;
										}
										if(($earm != 17 && $ecno == 11) || ($esub1_ex != 5 && $ecno == 14) || ($esub1_ex != 7 && $ecno == 16) || ($esub1_ex != 11 && $ecno == 15) || ($earm != 18 && $ecno == 12) || ($earm != 19 && $ecno == 13)){
											$ecno = 0;
											$eccp = 0;
											$erap = 0;
										}
										if($ksol <= 0){last;}

										if($last_battle eq "0"){
										($kcname,$kcno,$kccp,$krap) = split(/<>/,$KCOM[$count]);
										($ecname,$ecno,$eccp,$erap) = split(/<>/,$ECOM[$count]);

				

										if($krap == 0 && ($erap == 1 || $erap == 2 || $erap == 3)){
										$flag = "��";
										$kjensul = -20;
										$ejensul = $W_JEN_SUL[$ecno];
										}elsif($erap == 0 && ($krap == 1 || $krap == 2 || $krap == 3)){
										$flag = "��";
										$kjensul = $W_JEN_SUL[$kcno];
										$ejensul = -20;
										}elsif(($krap == 0 && $erap == 0) || ($krap == 1 && $erap == 1) || ($krap == 2 && $erap == 2) || ($krap == 3 && $erap == 3)){
										$flag = "��";
										$kjensul = 0;
										$ejensul = 0;
										}elsif(($krap == 1 && $erap == 2) || ($krap == 2 && $erap == 3) || ($krap == 3 && $erap == 1)){
										if($esub1_ex == 7 && $ecno == 16){
											$esol += 200;
											&K_LOG3("<font color=red>$count</font>��:������ �ߵ�! ������ ���簡 <font color=blue>+200</font> ���!");
											&E_LOG3("<font color=red>$count</font>��:������ �ߵ�! �Ʊ��� ���簡 <font color=blue>+200</font> ���!");
										}
										if($earm == 18 && $ecno == 12){
											$edamage = int($katt * 0.4);
											&K_LOG3("<font color=red>$count</font>��:��õ�� �ߵ�! �Ʊ��� ���ݷ��� <font color=blue>$edamage</font> ����!");
											&E_LOG3("<font color=red>$count</font>��:��õ�� �ߵ�! ���� ���ݷ��� <font color=blue>$edamage</font> ����!");
										}
										$flag = "��";
										$kjensul = $L_JEN_SUL[$kcno];
										$ejensul = $W_JEN_SUL[$ecno];
										}elsif(($erap == 1 && $krap == 2) || ($erap == 2 && $krap == 3) || ($erap == 3 && $krap == 1)){
										if($ksub1_ex == 11 && $kcno == 15){
											$egat -= 10;
											&K_LOG3("<font color=red>$count</font>��:�Ŷ���� �ߵ�! �� ����� �Ʒõ��� ��Ҵ�!");
											&E_LOG3("<font color=red>$count</font>��:�Ŷ���� �ߵ�! �� ������� �Ʒõ��� �𿴴�!");
										}
										if($karm == 19 && $kcno == 13){
											$ego_ex += 70;
											&K_LOG3("<font color=red>$count</font>��:ź���� �ߵ�! �� ������� ��ó�� ������!");
											&E_LOG3("<font color=red>$count</font>��:ź���� �ߵ�! �� ������� ��ó�� �Ծ���!");
										}
										$flag = "��";
										$kjensul = $W_JEN_SUL[$kcno];
										$ejensul = $L_JEN_SUL[$ecno];
										}
										$kdmg = int((rand($katt*1.5) - $edamage) * (($SOL_TYPE1[$ksub1_ex]+$kjensul)/100));
										$edmg = int(rand($eatt*1.5)*(($SOL_TYPE1[$esub1_ex]+$ejensul)/100));

										$kjihyng = int($SOL_TYPE1[$ksub1_ex]+$kjensul);
										$ejihyng = int($SOL_TYPE1[$esub1_ex]+$ejensul);

										}elsif($last_battle eq "1"){
										$flag = "VS";
										$kdmg = int(rand($katt*2)+$kdmg1);
										$edmg = int(rand($eatt*2)+$edmg1);

										$padmg = int(5+rand(5));
										if($ksub1_ex == 17 && $last_battle == 1){
										$zdef_att -= $padmg;
										$gmd = "/���ü� $zdef_att(-$padmg\)";
										}
										}
										


										if(($kdmg eq ""  || $kdmg < 1) && $ksuk < 1){
											$kdmg=1;	
										}elsif($kdmg < $ksuk){
										if($ksuk > $katt){
										$kdmg=$katt;}else{$kdmg=$ksuk;}
										}
										$wsol = $esol;
										$esol -= $kdmg;
										

										if($last_battle eq "0"){
										$kex_add += ($wsol - $esol);
										}elsif($last_battle eq "1"){
										$kex_add += int(($wsol - $esol)/5);
										}
										
										if($esol <= 0){
											$esol=0;
											&K_LOG3("<font color=red>$count</font>��:$kname�� $SOL_TYPE[$ksub1_ex]�δ� $ksol�� (-$edmg\)$kjihyng $flag $ename�� $SOL_TYPE[$esub1_ex]�δ� $esol�� (-$kdmg\)$gmd$kskilldmg$ejihyng");
											&E_LOG3("<font color=red>$count</font>��:$kname�� $SOL_TYPE[$ksub1_ex]�δ� $ksol�� (-$edmg\)$kjihyng $flag $ename�� $SOL_TYPE[$esub1_ex]�δ� $esol�� (-$kdmg\)$ejihyng");
											$win = 1;
										last;
										}
										
										if(($edmg eq "" || $edmg < 1) && $esuk < 1){
											$edmg=1;	
										}elsif($edmg < $esuk){
										if($esuk > $eatt){
										$edmg=$eatt;}else{$edmg=$esuk;}
										}
										$wsol = $ksol;
										$ksol -= $edmg;
										$eex_add += ($wsol - $ksol);
										if($ksol <= 0){
											$ksol=0;
											&K_LOG3("<font color=red>$count</font>��:$kname�� $SOL_TYPE[$ksub1_ex]�δ� $ksol�� (-$edmg\)$kjihyng $flag $ename�� $SOL_TYPE[$esub1_ex]�δ� $esol�� (-$kdmg\)$gmd$kskilldmg$ejihyng");
											&E_LOG3("<font color=red>$count</font>��:$kname�� $SOL_TYPE[$ksub1_ex]�δ� $ksol�� (-$edmg\)$kjihyng $flag $ename�� $SOL_TYPE[$esub1_ex]�δ� $esol�� (-$kdmg\)$ejihyng");
											last;
										}

										&K_LOG3("<font color=red>$count</font>��:$kname�� $SOL_TYPE[$ksub1_ex]�δ� $ksol�� (-$edmg\)$kjihyng $flag $ename�� $SOL_TYPE[$esub1_ex]�δ� $esol�� (-$kdmg\)$gmd$kskilldmg$ejihyng");
									}

									$eex_add = int($eex_add/40);
									$kex_add = int($kex_add/40);
									$kex_add1 = int($kex_add/350);
									$eex_add1 = int($eex_add/350);
									if($win){
										$ksub2_ex++;
										if($last_battle){
											if($town_get[$zcon] <= 1){
												@NEW_COU=();
												foreach(@COU_DATA){
													($xcid,$xname,$xele,$xmark,$xking,$xmes,$xsub,$xpri)=split(/<>/);
													if("$zcon" eq "$xcid"){
													}else{
														push(@NEW_COU,"$_");
													}
												}
												open(OUT,">$COUNTRY_LIST");
												print OUT @NEW_COU;
												close(OUT);
												&MAP_LOG2("<img src=$IMG/j3.gif> \[$old_date\]$cou_name[$zcon]���� ����߽��ϴ�.");
												&MAP_LOG("<img src=$IMG/j3.gif> \[$old_date\]$cou_name[$zcon]���� ����߽��ϴ�.");
											}


											$zcon = $kcon;
											$znou = int($znou*0.8);
											$zsyo = int($zsyo*0.8);
											$zsub1 = int($zsub1*0.8);
											$zshiro += 100;
											$zpri = int($zpri*0.8);
											$zdef_att = int($zdef_att*0.8);
											$zbong1 = "";
											$zbong2 = "";
											$zbong3 = "";
											$kex_add += 80;
											$kcex += $kex_add;
											$kexp += $kex_add;
											$kpoint += $kex_add1;
											$kpos = $cnum;

											@NEW_DEF_LIST3=();
											$pphit=0;
											foreach(@DEF_LIST3){
												($did,$dname,$dtown_id,$dtown_flg,$dcon,$dchara,$dsol,$dsub1_ex,$dtown_battle,$ddef) = split(/<>/);
												if("$did" eq "$kid"){
													$pphit=1;													unshift(@NEW_DEF_LIST3,"$kid<>$kname<>$kpos<>0<>$kcon<>$kchara<>$ksol<>$ksub1_ex<>0<>\n");
												}else{
													push(@NEW_DEF_LIST3,"$_");
												}
											}


											if(!$pphit){
												unshift(@NEW_DEF_LIST3,"$kid<>$kname<>$kpos<>0<>$kcon<>$kchara<>$ksol<>$ksub1_ex<>0<>\n");
											}
											open(OUT,">$DEF_LIST");
											print OUT @NEW_DEF_LIST3;
											close(OUT);



											&K_LOG2("<font color=blue>$zname</font>�� �տ� �־���! <font color=red>$kex_add</font>�� ����ġ�� ������ϴ�!");
											&HISTORY_LOG($kid,"<font color=blue>$zname</font>�� �տ� �־���!");
											&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth�� : $kname�� �δ밡 $zname���� �����ߴ�!</font>");
											&MAP_LOG2("<img src=$IMG/j4.gif> \[$old_date\]$cou_name[$kcon]���� $kname�δ�� $zname���� �����߽��ϴ�!");
											&MAP_LOG("<img src=$IMG/j4.gif> $cou_name[$kcon]���� $kname�δ�� $zname�� �����߽��ϴ�!");
										}else{
											@NEW_DEF_LIST3=();
											foreach(@DEF_LIST3){
												($did,$dname,$dtown_id,$dtown_flg,$dcon,$dchara,$dsol,$dsub1_ex,$dtown_battle,$ddef) = split(/<>/);
												if("$mdid" ne "$did"){
													push(@NEW_DEF_LIST3,"$_");
												}
											}
											open(OUT,">$DEF_LIST");
											print OUT @NEW_DEF_LIST3;
											close(OUT);

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
										if($qtalkd eq ""){
										}else{
										&K_LOG("$mmonth�� : $qtalkd");
										}
										}
									}	
								}
							}

											$kex_add += 50;
											$eex_add += 15;
											$kcex += int($kex_add * 0.8);
											$kexp += int($kex_add * 0.8);
											$kgg = int($kex_add * 0.8);
											$kpoint += $kex_add1;
											$ecex += int($eex_add * 0.6);
											$eexp += int($kex_add * 0.6);
											$egg = int($eex_add * 0.6);
											$epoint += $eex_add1;
											$esol = 0;
											$egat = 0;
											$kqpoint += 1 if $kcodea =~ /A9|C8/;
											&K_LOG2("\[$old_date\] $kname�� $SOL_TYPE[$ksub1_ex]�δ�� $ename�� $SOL_TYPE[$esub1_ex]�δ븦 ������׽��ϴ�! <font color=blue>$kgg</font>�� ����ġ�� ������ϴ�!");
											&E_LOG2("\[$old_date\] $ename�� $SOL_TYPE[$esub1_ex]�δ�� $kname�� $SOL_TYPE[$ksub1_ex]�δ뿡�� �й��ߴ�. <font color=red>$egg</font>�� ����ġ�� ������ϴ�!");
											&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth�� : $kname�� �δ�� ������̴� $ename�� �δ븦 ���������� �����Ų ����̴�.</font>");
											&MAP_LOG("<img src=$IMG/j5.gif> $kname�� $SOL_TYPE[$ksub1_ex]�δ�� $ename�� $SOL_TYPE[$esub1_ex]�δ븦 ������׽��ϴ�!");
										}
									}else{
											$esub2_ex++;
											@NEW_DEF_LIST3=();
											$dnum = 0;
											foreach(@DEF_LIST3){
												($did,$dname,$dtown_id,$dtown_flg,$dcon,$dchara,$dsol,$dsub1_ex,$dtown_battle,$ddef) = split(/<>/);
												if("$kid" ne "$did"){
													push(@NEW_DEF_LIST3,"$_");
												}
												if($eid eq "$did"){
													$ddef++;
													splice(@NEW_DEF_LIST3,$dnum,1,"$did<>$dname<>$dtown_id<>$dtown_flg<>$dcon<>$dchara<>$esol<>$dsub1_ex<>1<>$ddef<>\n");
												}
												$dnum++;
											}
											open(OUT,">$DEF_LIST");
											print OUT @NEW_DEF_LIST3;
											close(OUT);

							open(IN,"$QUEST_DATA");
							@QUEST_DATA = <IN>;
							close(IN);

							foreach(@QUEST_DATA){
							($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
								if($ecodea =~ /$qcode/ && $qrate > rand(99)){
									if($qcategory =~ /����/){
										$eqpoint += $qup;
										if($qtalkd eq ""){
										}else{
										&E_LOG("$mmonth�� : $qtalkd");
										}
									}	
								}
							}

										$eex_add += 50;
										$kex_add += 15;
										$ecex += $eex_add;
										$kcex += $kex_add;
										$eexp += $eex_add;
										$kexp += $kex_add;
										$epoint += $eex_add1;
										$kpoint += $kex_add1;
										if($gg < 30){
										$kgat = 0;
										}
										&K_LOG2("\[$old_date\] $kname�� $SOL_TYPE[$ksub1_ex]�δ�� $ename�� $SOL_TYPE[$esub1_ex]�δ뿡�� �й��ߴ�.. <font color=red>$kex_add</font>�� ����ġ�� ������ϴ�!");
										&E_LOG2("\[$old_date\] $ename�� $SOL_TYPE[$esub1_ex]�δ�� $kname�� $SOL_TYPE[$ksub1_ex]�δ븦 ������״�!! <font color=blue>$eex_add</font>�� ����ġ�� ������ϴ�!");
										&BATTLE_LOG("<font color=$ELE_C[$cou_ele[$kcon]]>$mmonth�� : $ename�� �δ�� ������ ������ $kname�� �δ븦 ������� �����Ų ����̴�.</font>");
									}

									if(!$last_battle){
										if($eid ne ""){
											&ENEMY_INPUT;
										}
									}else{
										$zshiro = $esol;
										if($ksub1_ex eq "12"){
										$zdef_att -= int($ksol/50);
										}else{
										$zdef_att -= int($ksol/100);
										}
										if($zdef_att < 0){
											$zdef_att=0;
										}
											splice(@TOWN_DATA,$cnum,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>$zname1<>$zname2<>$zbong1<>$zbong2<>$zbong3<>\n");
									}


									&BATTLE_LOG("<HR NOSHADE SIZE=3>");
									$kstr_ex++;
									$go_ex += int($kbank/5);
									$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
								}
							}
						}	
}
1;

