subroutine bouncing_pstick(dv, m, ps, Nr, Nm)
   ! Subroutine computes the sticking probabilities including sticking-bouncing transition of Windmark et al. (2012).
   !
   ! Parameters
   ! ----------
   ! dv(Nr, Nm, Nm) : Relative velocities
   ! m(Nm) : Mass grid
   ! Nr : Number of radial grid cells
   ! Nm : Number of mass bins
   ! Returns
   ! -------
   ! ps(Nr, Nm, Nm) : Sticking probabilities

   implicit none

   double precision, intent(in)  :: dv(Nr, Nm, Nm)
   double precision, intent(in)  :: m(Nm)
   double precision, intent(out) :: ps(Nr, Nm, Nm)
   integer,          intent(in)  :: Nr
   integer,          intent(in)  :: Nm

   double precision :: k0
   double precision :: k1
   double precision :: k2
   double precision :: mb
   double precision :: ms
   double precision :: p(Nr)

   integer :: i
   integer :: j

   mb = 3.3d-3
   ms = 3.0d-12

   k0 = LOG10(mb/ms)
   k1 = 3.6d0/k0

   ps(:, :, :) = 0.d0

   do i=1, Nm
      do j=1, i
         k2 = LOG10(m(j)/ms)/k0
         p(:) = MIN(1.d0 - k1*LOG10(dv(:, j, i)) - k2, 1.d0)
         ps(:, i, j) = MAX(0.d0, p(:))
         ps(:, j, i) = ps(:, i, j)
      end do
   end do

end subroutine bouncing_pstick