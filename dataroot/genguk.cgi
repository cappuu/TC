
sub GENGUK{
				$ksub2=0;
				if($zcon != 0){
					&K_LOG("�� ���ÿ����� ����� �� �����ϴ�.");
				}elsif($csub != $kpos){
					&K_LOG("�������� �ٸ��ϴ�.");
				}else{
					foreach(@COU_DATA){
						($xcid,$xname,$xele,$xmark,$xking,$xmes,$xsub,$xpri)=split(/<>/);
						$ele{$xele} = 1;
					}
					while(){
						$rnd_max = @ELE_C-1;
						$r = int(rand($rnd_max))+1;
						if( $ele{$r} != 1 ){
							$cend = $r;
							last;
						}
					}
					$COU_NO_DATA++;
					$kcon = $COU_NO_DATA;
					$zcon = $COU_NO_DATA;
					push(@COU_DATA,"$new_cou_no<>$in{'cou_name'}<>$in{'ele'}<>1<>$in{'id'}<><>$in{'chara_name'}<>1<>\n");

					&K_LOG("$mmonth�� : $cnum���� �Ǳ��߽��ϴ�.");
					&MAP_LOG2("<font color=000088><B>[�Ǳ�]</B></font> $kname���� $cnum���� �Ǳ��Ͽ����ϴ�.");
					&MAP_LOG("<font color=000088><B>[�Ǳ�]</B></font> $kname���� $zname���� �������� �� $cnum���� �Ǳ��Ͽ����ϴ�.");
					&HISTORY_LOG($kid,"$cnum���� �Ǳ��Ͽ����ϴ�.");
					&TOWN_CHANGE($kpos);
				}	
}
1;

