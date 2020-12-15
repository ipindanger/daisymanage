 i m p o r t   h t m l 
 f r o m   t e l e g r a m   i m p o r t   C h a t ,   U s e r ,   P a r s e M o d e 
 f r o m   t e l e g r a m . e r r o r   i m p o r t   B a d R e q u e s t 
 f r o m   t e l e g r a m . u t i l s . h e l p e r s   i m p o r t   m e n t i o n _ h t m l 
 f r o m   t e l e g r a m   i m p o r t   P a r s e M o d e 
 f r o m   t e l e g r a m . e x t   i m p o r t   ( r u n _ a s y n c , 
                                                     F i l t e r s ,   C o m m a n d H a n d l e r ) 
 
 f r o m   S a i t a m a R o b o t   i m p o r t   d i s p a t c h e r ,   R E D I S 
 f r o m   S a i t a m a R o b o t . m o d u l e s . d i s a b l e   i m p o r t   D i s a b l e A b l e C o m m a n d H a n d l e r 
 f r o m   S a i t a m a R o b o t . m o d u l e s . h e l p e r _ f u n c s . c h a t _ s t a t u s   i m p o r t   ( 
         b o t _ a d m i n , 
         u s e r _ a d m i n 
 ) 
 f r o m   S a i t a m a R o b o t . m o d u l e s . h e l p e r _ f u n c s . e x t r a c t i o n   i m p o r t   e x t r a c t _ u s e r _ a n d _ t e x t 
 f r o m   S a i t a m a R o b o t . m o d u l e s . h e l p e r _ f u n c s . a l t e r n a t e   i m p o r t   t y p i n g _ a c t i o n 
 
 
 
 
 @ r u n _ a s y n c 
 @ t y p i n g _ a c t i o n 
 d e f   a p p r o v e l ( u p d a t e ,   c o n t e x t ) : 
         c h a t   =   u p d a t e . e f f e c t i v e _ c h a t     
         u s e r   =   u p d a t e . e f f e c t i v e _ u s e r   
         m e s s a g e   =   u p d a t e . e f f e c t i v e _ m e s s a g e 
         a r g s   =   c o n t e x t . a r g s   
         u s e r _ i d ,   r e a s o n   =   e x t r a c t _ u s e r _ a n d _ t e x t ( m e s s a g e ,   a r g s ) 
         i f   n o t   u s e r _ i d : 
                 m e s s a g e . r e p l y _ t e x t ( " Y o u   d o n ' t   s e e m   t o   b e   r e f e r r i n g   t o   a   u s e r . " ) 
                 r e t u r n   
         t r y : 
                 m e m b e r   =   c h a t . g e t _ m e m b e r ( u s e r _ i d ) 
         e x c e p t   B a d R e q u e s t   a s   e x c p : 
                 i f   e x c p . m e s s a g e   = =   " U s e r   n o t   f o u n d " : 
                         m e s s a g e . r e p l y _ t e x t ( " I   c a n ' t   s e e m   t o   f i n d   t h i s   u s e r " ) 
                         r e t u r n   
                 e l s e : 
                         r a i s e 
         i f   u s e r _ i d   = =   c o n t e x t . b o t . i d : 
                 m e s s a g e . r e p l y _ t e x t ( " H o w   I   s u p p o s e d   t o   a p p r o v e   m y s e l f " ) 
                 r e t u r n   
         
         c h a t _ i d   =   s t r ( c h a t . i d ) [ 1 : ]   
         a p p r o v e _ l i s t   =   l i s t ( R E D I S . s u n i o n ( f ' a p p r o v e _ l i s t _ { c h a t _ i d } ' ) ) 
         t a r g e t _ u s e r   =   m e n t i o n _ h t m l ( m e m b e r . u s e r . i d ,   m e m b e r . u s e r . f i r s t _ n a m e ) 
         i f   t a r g e t _ u s e r   i n   a p p r o v e _ l i s t : 
                 m e s s a g e . r e p l y _ t e x t ( 
                         " { }   i s   a n   a p p r o v e d   u s e r .   L o c k s ,   a n t i f l o o d ,   a n d   b l o c k l i s t s   w o n ' t   a p p l y   t o   t h e m . " . f o r m a t ( m e n t i o n _ h t m l ( m e m b e r . u s e r . i d ,   m e m b e r . u s e r . f i r s t _ n a m e ) ) ,                                                                                             
                         p a r s e _ m o d e = P a r s e M o d e . H T M L 
                 ) 
                 r e t u r n 
 
         i f   t a r g e t _ u s e r   n o t   i n   a p p r o v e _ l i s t : 
                 m e s s a g e . r e p l y _ t e x t ( 
                         " { }   i s   n o t   a n   a p p r o v e d   u s e r .   T h e y   a r e   a f f e c t e d   b y   n o r m a l   c o m m a n d s . " . f o r m a t ( m e n t i o n _ h t m l ( m e m b e r . u s e r . i d ,   m e m b e r . u s e r . f i r s t _ n a m e ) ) ,                                                                                             
                         p a r s e _ m o d e = P a r s e M o d e . H T M L 
                 ) 
                 r e t u r n 
 
 
 
 @ r u n _ a s y n c 
 @ b o t _ a d m i n 
 @ u s e r _ a d m i n 
 @ t y p i n g _ a c t i o n 
 d e f   a p p r o v e ( u p d a t e ,   c o n t e x t ) : 
         c h a t   =   u p d a t e . e f f e c t i v e _ c h a t     
         u s e r   =   u p d a t e . e f f e c t i v e _ u s e r   
         m e s s a g e   =   u p d a t e . e f f e c t i v e _ m e s s a g e 
         a r g s   =   c o n t e x t . a r g s   
         u s e r _ i d ,   r e a s o n   =   e x t r a c t _ u s e r _ a n d _ t e x t ( m e s s a g e ,   a r g s ) 
         i f   n o t   u s e r _ i d : 
                 m e s s a g e . r e p l y _ t e x t ( " Y o u   d o n ' t   s e e m   t o   b e   r e f e r r i n g   t o   a   u s e r . " ) 
                 r e t u r n   
         t r y : 
                 m e m b e r   =   c h a t . g e t _ m e m b e r ( u s e r _ i d ) 
         e x c e p t   B a d R e q u e s t   a s   e x c p : 
                 i f   e x c p . m e s s a g e   = =   " U s e r   n o t   f o u n d " : 
                         m e s s a g e . r e p l y _ t e x t ( " I   c a n ' t   s e e m   t o   f i n d   t h i s   u s e r " ) 
                         r e t u r n   
                 e l s e : 
                         r a i s e 
         i f   u s e r _ i d   = =   c o n t e x t . b o t . i d : 
                 m e s s a g e . r e p l y _ t e x t ( " H o w   I   s u p p o s e d   t o   a p p r o v e   m y s e l f " ) 
                 r e t u r n   
         
         c h a t _ i d   =   s t r ( c h a t . i d ) [ 1 : ]   
         a p p r o v e _ l i s t   =   l i s t ( R E D I S . s u n i o n ( f ' a p p r o v e _ l i s t _ { c h a t _ i d } ' ) ) 
         t a r g e t _ u s e r   =   m e n t i o n _ h t m l ( m e m b e r . u s e r . i d ,   m e m b e r . u s e r . f i r s t _ n a m e ) 
         i f   t a r g e t _ u s e r   i n   a p p r o v e _ l i s t : 
                 m e s s a g e . r e p l y _ t e x t ( 
                         " { }   i s   a l r e a d y   a p p r o v e d   i n   { } . " . f o r m a t ( m e n t i o n _ h t m l ( m e m b e r . u s e r . i d ,   m e m b e r . u s e r . f i r s t _ n a m e ) , 
                                                                                                                       c h a t . t i t l e ) , 
                         p a r s e _ m o d e = P a r s e M o d e . H T M L 
                 ) 
                 r e t u r n 
         m e m b e r   =   c h a t . g e t _ m e m b e r ( i n t ( u s e r _ i d ) ) 
         c h a t _ i d   =   s t r ( c h a t . i d ) [ 1 : ] 
         R E D I S . s a d d ( f ' a p p r o v e _ l i s t _ { c h a t _ i d } ' ,   m e n t i o n _ h t m l ( m e m b e r . u s e r . i d ,   m e m b e r . u s e r . f i r s t _ n a m e ) ) 
         m e s s a g e . r e p l y _ t e x t ( 
                 " { }   h a s   b e e n   a p p r o v e d   i n   { } . " . f o r m a t ( m e n t i o n _ h t m l ( m e m b e r . u s e r . i d ,   m e m b e r . u s e r . f i r s t _ n a m e ) , 
                                                                                                                                           c h a t . t i t l e ) , 
                 p a r s e _ m o d e = P a r s e M o d e . H T M L ) 
         
         
 
 @ r u n _ a s y n c 
 @ b o t _ a d m i n 
 @ u s e r _ a d m i n 
 @ t y p i n g _ a c t i o n 
 d e f   u n a p p r o v e ( u p d a t e ,   c o n t e x t ) : 
         c h a t   =   u p d a t e . e f f e c t i v e _ c h a t     
         u s e r   =   u p d a t e . e f f e c t i v e _ u s e r   
         m e s s a g e   =   u p d a t e . e f f e c t i v e _ m e s s a g e 
         a r g s   =   c o n t e x t . a r g s   
         u s e r _ i d ,   r e a s o n   =   e x t r a c t _ u s e r _ a n d _ t e x t ( m e s s a g e ,   a r g s ) 
         i f   n o t   u s e r _ i d : 
                 m e s s a g e . r e p l y _ t e x t ( " Y o u   d o n ' t   s e e m   t o   b e   r e f e r r i n g   t o   a   u s e r . " ) 
                 r e t u r n   
         t r y : 
                 m e m b e r   =   c h a t . g e t _ m e m b e r ( u s e r _ i d ) 
         e x c e p t   B a d R e q u e s t   a s   e x c p : 
                 i f   e x c p . m e s s a g e   = =   " U s e r   n o t   f o u n d " : 
                         m e s s a g e . r e p l y _ t e x t ( " I   c a n ' t   s e e m   t o   f i n d   t h i s   u s e r " ) 
                         r e t u r n   
                 e l s e : 
                         r a i s e 
         i f   u s e r _ i d   = =   c o n t e x t . b o t . i d : 
                 m e s s a g e . r e p l y _ t e x t ( " h o w   I   s u p p o s e d   t o   a p p r o v e   o r   u n a p p r o v e   m y s e l f " ) 
                 r e t u r n   
         c h a t _ i d   =   s t r ( c h a t . i d ) [ 1 : ]   
         a p p r o v e _ l i s t   =   l i s t ( R E D I S . s u n i o n ( f ' a p p r o v e _ l i s t _ { c h a t _ i d } ' ) ) 
         t a r g e t _ u s e r   =   m e n t i o n _ h t m l ( m e m b e r . u s e r . i d ,   m e m b e r . u s e r . f i r s t _ n a m e ) 
         i f   t a r g e t _ u s e r   n o t   i n   a p p r o v e _ l i s t : 
                 m e s s a g e . r e p l y _ t e x t ( 
                         " { }   i s n ' t   a p p r o v e d   y e t . " . f o r m a t ( m e n t i o n _ h t m l ( m e m b e r . u s e r . i d ,   m e m b e r . u s e r . f i r s t _ n a m e ) ) , 
                         p a r s e _ m o d e = P a r s e M o d e . H T M L 
                 ) 
                 r e t u r n 
         m e m b e r   =   c h a t . g e t _ m e m b e r ( i n t ( u s e r _ i d ) ) 
         c h a t _ i d   =   s t r ( c h a t . i d ) [ 1 : ] 
         R E D I S . s r e m ( f ' a p p r o v e _ l i s t _ { c h a t _ i d } ' ,   m e n t i o n _ h t m l ( m e m b e r . u s e r . i d ,   m e m b e r . u s e r . f i r s t _ n a m e ) ) 
         m e s s a g e . r e p l y _ t e x t ( 
                 " { }   i s   n o   l o n g e r   a p p r o v e d   i n   { } . " . f o r m a t ( m e n t i o n _ h t m l ( m e m b e r . u s e r . i d ,   m e m b e r . u s e r . f i r s t _ n a m e ) , 
                                                                                                                                           c h a t . t i t l e ) , 
                 p a r s e _ m o d e = P a r s e M o d e . H T M L 
         ) 
 
         
 @ r u n _ a s y n c 
 @ b o t _ a d m i n 
 @ u s e r _ a d m i n 
 @ t y p i n g _ a c t i o n 
 d e f   a p p r o v e d ( u p d a t e ,   c o n t e x t ) : 
         c h a t   =   u p d a t e . e f f e c t i v e _ c h a t   
         u s e r   =   u p d a t e . e f f e c t i v e _ u s e r   
         m e s s a g e   =   u p d a t e . e f f e c t i v e _ m e s s a g e 
         c h a t _ i d   =   s t r ( c h a t . i d ) [ 1 : ]   
         a p p r o v e d _ l i s t   =   l i s t ( R E D I S . s u n i o n ( f ' a p p r o v e _ l i s t _ { c h a t _ i d } ' ) ) 
         a p p r o v e d _ l i s t . s o r t ( ) 
         a p p r o v e d _ l i s t   =   " ,   " . j o i n ( a p p r o v e d _ l i s t ) 
         
         i f   a p p r o v e d _ l i s t :   
                         m e s s a g e . r e p l y _ t e x t ( 
                                 " T h e   F o l l o w i n g   U s e r s   A r e   A p p r o v e d :   \ n " 
                                 " { } " . f o r m a t ( a p p r o v e d _ l i s t ) , 
                                 p a r s e _ m o d e = P a r s e M o d e . H T M L 
                         ) 
         e l s e : 
                 m e s s a g e . r e p l y _ t e x t ( 
                         " N o   u s e r s   a r e   a r e   a p p r o v e d   i n   { } . " . f o r m a t ( c h a t . t i t l e ) , 
                                 p a r s e _ m o d e = P a r s e M o d e . H T M L 
                 ) 
 
 @ r u n _ a s y n c 
 @ b o t _ a d m i n 
 @ u s e r _ a d m i n 
 @ t y p i n g _ a c t i o n 
 d e f   u n a p p r o v e a l l ( u p d a t e ,   c o n t e x t ) : 
         c h a t   =   u p d a t e . e f f e c t i v e _ c h a t   
         u s e r   =   u p d a t e . e f f e c t i v e _ u s e r   
         m e s s a g e   =   u p d a t e . e f f e c t i v e _ m e s s a g e 
         c h a t _ i d   =   s t r ( c h a t . i d ) [ 1 : ]   
         a p p r o v e _ l i s t   =   l i s t ( R E D I S . s u n i o n ( f ' a p p r o v e _ l i s t _ { c h a t _ i d } ' ) ) 
         f o r   t a r g e t _ u s e r   i n   a p p r o v e _ l i s t : 
                 R E D I S . s r e m ( f ' a p p r o v e _ l i s t _ { c h a t _ i d } ' ,   t a r g e t _ u s e r ) 
         m e s s a g e . r e p l y _ t e x t ( 
                 " S u c c e s s u l l y   u n a p p r o v e d   a l l   u s e r s   f r o m   { } . " . f o r m a t ( c h a t . t i t l e ) 
         ) 
                 
 _ _ m o d _ n a m e _ _   =   " A p p r o v a l "         
 
 _ _ h e l p _ _   =   " " "   
 \ 
 S o m e t i m e s ,   y o u   m i g h t   t r u s t   a   u s e r   n o t   t o   s e n d   u n w a n t e d   c o n t e n t . 
 M a y b e   n o t   e n o u g h   t o   m a k e   t h e m   a d m i n ,   b u t   y o u   m i g h t   b e   o k   w i t h   l o c k s ,   b l a c k l i s t s ,   a n d   a n t i f l o o d   n o t   a p p l y i n g   t o   t h e m . 
 
 T h a t ' s   w h a t   a p p r o v a l s   a r e   f o r   -   a p p r o v e   o f   t r u s t w o r t h y   u s e r s   t o   a l l o w   t h e m   t o   s e n d   
 
 A d m i n   c o m m a n d s : 
 -   / a p p r o v a l :   C h e c k   a   u s e r ' s   a p p r o v a l   s t a t u s   i n   t h i s   c h a t . 
 
 A d m i n   c o m m a n d s : 
 -   / a p p r o v e :   A p p r o v e   o f   a   u s e r .   L o c k s ,   b l a c k l i s t s ,   a n d   a n t i f l o o d   w o n ' t   a p p l y   t o   t h e m   a n y m o r e . 
 -   / u n a p p r o v e :   U n a p p r o v e   o f   a   u s e r .   T h e y   w i l l   n o w   b e   s u b j e c t   t o   l o c k s ,   b l a c k l i s t s ,   a n d   a n t i f l o o d   a g a i n . 
 -   / a p p r o v e d :   L i s t   a l l   a p p r o v e d   u s e r s . 
 -   / u n a p p r o v e a l l :   U n a p p r o v e   A L L   u s e r s   i n   a   c h a t .   T h i s   c a n n o t   b e   u n d o n e . 
 \ 
 " " "         
 
 A P P R O V E D _ H A N D L E R   =   D i s a b l e A b l e C o m m a n d H a n d l e r ( " a p p r o v e d " ,   a p p r o v e d ,   f i l t e r s = F i l t e r s . g r o u p ) 
 U N A P P R O V E _ A L L _ H A N D L E R   =   D i s a b l e A b l e C o m m a n d H a n d l e r ( " u n a p p r o v e a l l " ,   u n a p p r o v e a l l ,   f i l t e r s = F i l t e r s . g r o u p ) 
 A P P R O V E _ H A N D L E R   =   D i s a b l e A b l e C o m m a n d H a n d l e r ( " a p p r o v e " ,   a p p r o v e ,   p a s s _ a r g s = T r u e ,   f i l t e r s = F i l t e r s . g r o u p ) 
 U N A P P R O V E _ H A N D L E R   =   D i s a b l e A b l e C o m m a n d H a n d l e r ( " u n a p p r o v e " ,   u n a p p r o v e ,   p a s s _ a r g s = T r u e ,   f i l t e r s = F i l t e r s . g r o u p ) 
 A P P R O V E L _ H A N D L E R   =   D i s a b l e A b l e C o m m a n d H a n d l e r ( " a p p r o v e l " ,   a p p r o v e l ,   p a s s _ a r g s = T r u e ,   f i l t e r s = F i l t e r s . g r o u p ) 
 
 
 d i s p a t c h e r . a d d _ h a n d l e r ( A P P R O V E D _ H A N D L E R ) 
 d i s p a t c h e r . a d d _ h a n d l e r ( U N A P P R O V E _ A L L _ H A N D L E R ) 
 d i s p a t c h e r . a d d _ h a n d l e r ( A P P R O V E _ H A N D L E R )   
 d i s p a t c h e r . a d d _ h a n d l e r ( U N A P P R O V E _ H A N D L E R )   
 d i s p a t c h e r . a d d _ h a n d l e r ( A P P R O V E L _ H A N D L E R )