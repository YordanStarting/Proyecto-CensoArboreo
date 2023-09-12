insert into public."p_Arbol" (geom,Id_arbol,longitud,latitud)
values (ST_GeomFromText('POINT(-76.526328 3.395025)',4326), 157, -76.526328,3.395025)

UPDATE public."p_Arbol" SET longitud = ST_X(geom);
UPDATE public."p_Arbol" SET latitud = ST_Y(geom);

ALTER TABLE public."p_Arbol" ADD X_MC double precision
ALTER TABLE public."p_Arbol" ADD Y_MC double precision

UPDATE public."p_Arbol" SET X_MC = ST_X(ST_Transform(geom,6249));
UPDATE public."p_Arbol" SET Y_MC = ST_Y(ST_Transform(geom,6249));

ALTER TABLE public."p_Arbol" ADD Barrio varchar(100)
SELECT  arb.id_arbol as id_arbol, B.barrio as Barrio FROM public."p_Arbol" as arb, public."Barrios_wgs" as B
WHERE St_intersects (arb.geom,B.geom) 
