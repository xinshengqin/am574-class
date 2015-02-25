subroutine setprob

    implicit none
    character*25 :: fname
    integer :: iunit
    real(kind=8) :: grav,beta

    common /cparam/ grav
    common /cqinit/ beta
 
    ! Set the gravitational constant grav
    ! Set beta for Gaussian intitial conditions
 
    iunit = 7
    fname = 'setprob.data'
    ! open the unit with new routine from Clawpack 4.4 to skip over
    ! comment lines starting with #:
    call opendatafile(iunit, fname)


    ! gravitational constant:
    read(7,*) grav

    ! beta for initial conditions:
    read(7,*) beta

end subroutine setprob
