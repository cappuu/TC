
sub PAGYEON2{
				$ksub2=0;
				$zhit=0;
				($zzname,$zzcon,$zznum,$zznou,$zzsyo,$zzshiro,$zznou_max,$zzsyo_max,$zzshiro_max,$zzpri,$zzx,$zzy,$zzsouba,$zzdef_att,$zzsub1,$zzsub2,$zz[0],$zz[1],$zz[2],$zz[3],$zz[4],$zz[5],$zz[6],$zz[7],$zzname1,$zzname2,$zzbong1,$zzbong2,$zzbong3) = split(/<>/,$TOWN_DATA[$cnum]);
				
	if($zzname eq "����" || $zzname eq "���" || $zzname eq "���" || $zzname eq "����" || $zzname eq "��" || $zzname eq "��â" || $zzname eq "�Ǿ�" || $zzname eq "��"){
				$znum_limit = 100000;
	}elsif($zzname eq "ȫ��" || $zzname eq "��" || $zzname eq "����" || $zzname eq "����" || $zzname eq "����" || $zzname eq "����" || $zzname eq "��" || $zzname eq "����" || $zzname eq "����" || $zzname eq "�Ϻ�" || $zzname eq "����" || $zzname eq "��" || $zzname eq "����"){
				$znum_limit = 80000;
	}elsif($zzname eq "����" || $zzname eq "����" || $zzname eq "����" || $zzname eq "����" || $zzname eq "���" || $zzname eq "����" || $zzname eq "����" || $zzname eq "�û�" || $zzname eq "��" || $zzname eq "�ܾ�" || $zzname eq "����" || $zzname eq "ȸ��" || $zzname eq "�����" || $zzname eq "���" || $zzname eq "����"){
				$znum_limit = 65000;
	}else{
				$znum_limit = 50000;
	}


				if($zzcon == $kcon &&($zz[0] eq $kpos || $zz[1] eq $kpos || $zz[2] eq $kpos || $zz[3] eq $kpos || $zz[4] eq $kpos || $zz[5] eq $kpos || $zz[6] eq $kpos || $zz[7] eq $kpos)){
					($gold,$rice) = split(/,/,$csub);
					if( $znum < $rice ){ $rice = $znum; }
					elsif($kleat<int($rice/100)){
					&K_LOG("$mmonth�� : ���� �ֹ��� �ʹ� �����ϴ�.");
					}elsif($kgold<int($rice/20)){
					&K_LOG("$mmonth�� : ���� �����մϴ�.");
					}elsif($rice > int($znum_limit-$zznum)){
					&K_LOG("$mmonth�� : $town_name[$cnum]���� �ֹε��� �ʹ� �����ϴ�. [������ġ] : $zname��");
					}else{
					$znum -= $rice;
					&TOWN_CHANGE($kpos);
					$kpos = $cnum;

					($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7],$zname1,$zname2,$zbong1,$zbong2,$zbong3) = split(/<>/,$TOWN_DATA[$kpos]);


					$znum += $rice;
					&TOWN_CHANGE($cnum);
					&K_LOG("$mmonth�� : $town_name[$cnum]������ �ֹε��� $rice���� ���ֽ��׽��ϴ�.");
					&MAP_LOG("<img src=$IMG/j28.gif> $kname���� $town_name[$cnum]������ �ֹε��� ���ֽ��׽��ϴ�.");
					$kcex += int($rice/200);
					$kexp += 30;
					$kgold -= int($rice/20);
					$kpoint += int($rice/1000);
					$klea_ex++;
					$go_ex += int($kbank/5);
					$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
					}
					}else{
					&K_LOG("$mmonth�� : $town_name[$cnum]������ ������ ���� �����ϴ�. [������ġ] : $zname��");
				}

}
1;

