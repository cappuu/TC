
sub PAGAE{
				$ksub2=0;
				($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7],$zname1,$zname2,$zbong1,$zbong2,$zbong3) = split(/<>/,$TOWN_DATA[$cnum]);
				if($zcon eq $kcon){
					&K_LOG("�ڱ��� �ı��� ���� �����ϴ�.");
				}elsif($z[0] ne $kpos && $z[1] ne $kpos && $z[2] ne $kpos && $z[3] ne $kpos && $z[4] ne $kpos && $z[5] ne $kpos && $z[6] ne $kpos && $z[7] ne $kpos ){
					&K_LOG("$zname������ �������� �ʰ� �ֽ��ϴ�.");
				}elsif($kgold<100){
					&K_LOG("�ڱݺ������� ������ �� �������ϴ�.");
				}else{
					$kgold-= 100;
					($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7],$zname1,$zname2,$zbong1,$zbong2,$zbong3) = split(/<>/,$TOWN_DATA[$cnum]);
					$d_hit=0;
					foreach(@DEF_DATA){
						($mdid,$mdname,$mdtown_id,$mdtown_flg,$mdcon,$mdchara,$dsol,$dsub1_ex) = split(/<>/);
						if($cnum eq $mdtown_id){
							$d_hit++;
						}
					}
					$rate = int(rand(int($kintt)+120-$zshiro/10-$d_hit*30));
					$rate2 = int(rand(2))*int(rand(2))*int(rand(2))*int(rand(2))*int(rand(2))*int(rand(2));
					if($zcon eq ""){
						&K_LOG("$mmonth�� : ������������ �峭ġ�� ���ô�^^; [��Ģ:�Ƿε� 100 ����, �� 1000 ����]");
						$kgold -= 900;
						$go_ex += 100;
					}elsif( $rate < 50 && $rate2 == 0 ){
						&K_LOG("$mmonth�� : ���ۿ��� �������� $zname���� �ı��� �� �������ϴ�.");
						&MAP_LOG("<img src=$IMG/j18.gif> $kname�� ���� $zname���� �ı������� �����߽��ϴ�.");
					}else{
						if($rate < 50){
							&MAP_LOG("<img src=$IMG/j18.gif> $kname�� ���� $zname���� �ı������� <font color=red>����</font>�Ͽ����ϴ�.");
						}else{
							&MAP_LOG("<img src=$IMG/j18.gif> �������� ���� $zname���� �ı��� <font color=red>����</font>�Ǿ����ϴ�.");
						}
						$zshiro_dmg = int(rand($zshiro*0.1)+$zshiro*0.1);
						$zshiro -= $zshiro_dmg;
						if($zshiro < 0){
						$zshiro = 0;
						}
						if("$zname" ne ""){
							splice(@TOWN_DATA,$cnum,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>$zname1<>$zname2<>$zbong1<>$zbong2<>$zbong3<>\n");
						}
						&K_LOG("$mmonth�� : $zname���� �ı��� �����Ͽ� ����� <font color=red>-$zshiro_dmg</font>���� ����Ͽ����ϴ�.");
						$kcex += 50;
						$kexp += 50;
						$kpoint += 15;
						$kint_ex += 3;
					}
					$go_ex += int($kbank/5);
					$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
				}
}
1;

