class Yin: pass 
class Yang: 
        def __del__(self): 
            print("Yang destruido") 
 
yin = Yin() 
yang = Yang() 
yin.yang = yang 
 
print(yang) 
print(yang is yin.yang) 
Yang.__del__(yang) 
print("?") 

#Solución: El del hace que el print al que está asociado tenga mayor importancia. Eso hacía que el (yang)que tenia detrás pertenezca a la clase Yang directamente. Poniendo la clase Yang delante hacemos que la interrogación se introduzca en la clase y no se ponga como opción principal.