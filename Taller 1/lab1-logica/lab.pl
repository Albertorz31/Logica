% Laboratorio N°1 de Lógica y Teoría de la Computación 2-2019
% Autores: - Diego Águila
%         - Carlos Alvarez
%         - Alberto Rodríguez
%         - Chun-Zen Yu



% ///////////// BASE DE CONOCIMIENTOS ///////////

coloracion(blanca,1).
coloracion(rosada,2).
coloracion(roja,3).
coloracion(negra,4).
coloracion(morada,5).

%Se define que una fruta es exportable cuando el calibre es mediano o grande con defectos apenas perceptibles
salida(exportable,1).
salida(frutaComercialMercadoInterno,2).
salida(desecho,3).

% desecho(X):=

% Calibre vs Diametros[mm], define cual es el tamaño de la fruta
% Calibre(tamaño de la fruta, calibre de la fruta)
calibre(chica,  18).
calibre(chica , 19).
calibre(chica , 20).
calibre(chica , 21).
calibre(chica , 22).
calibre(mediana, 23).
calibre(mediana, 24).
calibre(mediana, 25).
calibre(mediana, 26).
calibre(mediana, 27).
calibre(grande, 28).
calibre(grande, 29).
calibre(grande, 30).
calibre(grande, 31).
calibre(grande, 32).

%Salida de Embalaje, indica cual es su linea de embalaje, segun su calibre
salidaLineaEmbalaje(1, 18).
salidaLineaEmbalaje(2, 19).
salidaLineaEmbalaje(3, 20).
salidaLineaEmbalaje(4, 21).
salidaLineaEmbalaje(5, 22).
salidaLineaEmbalaje(6, 23).
salidaLineaEmbalaje(7, 24).
salidaLineaEmbalaje(8, 25).
salidaLineaEmbalaje(9, 26).
salidaLineaEmbalaje(10, 27).
salidaLineaEmbalaje(11, 28).
salidaLineaEmbalaje(12, 29).
salidaLineaEmbalaje(13, 30).
salidaLineaEmbalaje(14, 31).
salidaLineaEmbalaje(15, 32).
salidaLineaEmbalaje(16, 33).

quemadura_solar(TipoMancha, NivelCobertura, R):-
    TipoMancha = quemadura_solar,
    (NivelCobertura = alto; NivelCobertura = medio),
    R = "quemadura solar".

fruto_doble(FrutoDoble, R):-
    (FrutoDoble == 1,
    R = "fruto doble");
    (FrutoDoble == 2,
    R = "fruto gemelo").

sin_color(Coloracion, R):-
    (Coloracion = blanca;
    Coloracion = rosada),
    R = "sin color".

sin_pedunculo(Pedunculo, R):-
    Pedunculo == 0,
    R = "sin pedunculo".

madurez_excesiva(Coloracion,Madurez):-
     Coloracion=negra,
     defecto(Madurez,1).
    
defecto_abrasion(TipoMancha, NivelCobertura, R):-
    TipoMancha = abrasion,
    (NivelCobertura = alto; NivelCobertura = medio),
    R = "defecto abrasion".

defecto_russet(TipoMancha, NivelCobertura, R):-
    TipoMancha = russet,
    (NivelCobertura = alto; NivelCobertura = medio),
    R = "defecto russet".

determinarCicatridura(PorcentajeCicatridura, Cicatridura):-
(PorcentajeCicatridura >= 10, PorcentajeCicatridura < 20, Cicatridura = "perforacion cicatrizada");
    (PorcentajeCicatridura >= 20, PorcentajeCicatridura < 40, Cicatridura = "cicatriz");
    (PorcentajeCicatridura >= 40, PorcentajeCicatridura < 60, Cicatridura = "media luna");
    (PorcentajeCicatridura >= 60, PorcentajeCicatridura < 80, Cicatridura = "partidura cicatrizada");
    (PorcentajeCicatridura >= 80, PorcentajeCicatridura < 100, Cicatridura = "herida cicatrizada").

determinarArrugado(PorcentajeArrugado, Cicatridura):-
    (PorcentajeArrugado >= 10, PorcentajeArrugado < 40, Cicatridura = "pitting");
    (PorcentajeArrugado >= 40, PorcentajeArrugado < 60, Cicatridura = "fruto arrugado");
    (PorcentajeArrugado >= 60, PorcentajeArrugado < 80, Cicatridura = "magulladura");
    (PorcentajeArrugado >= 80, PorcentajeArrugado < 100, Cicatridura = "machucon").

determinarColoracion(PorcentajeColoracion,Coloracion):-
    (PorcentajeColoracion >= 0, PorcentajeColoracion < 20, coloracion(Coloracion,1));
    (PorcentajeColoracion >= 20, PorcentajeColoracion < 40, coloracion(Coloracion,2));
    (PorcentajeColoracion >= 40, PorcentajeColoracion < 60, coloracion(Coloracion,3));
    (PorcentajeColoracion >= 60, PorcentajeColoracion < 80, coloracion(Coloracion,4));
    (PorcentajeColoracion >= 80, PorcentajeColoracion < 100, coloracion(Coloracion,5)).


% Funcion para detectar defectos
detectarDefectos(Coloracion, TipoMancha, NivelCobertura, PorcentajeCicatridura, PorcentajeArrugado, Pedunculo, FrutoDoble, Defecto):-
      madurez_excesiva(Coloracion,Defecto);
      sin_color(Coloracion,Defecto);
      quemadura_solar(TipoMancha, NivelCobertura, Defecto);
      defecto_abrasion(TipoMancha, NivelCobertura, Defecto);
      defecto_russet(TipoMancha, NivelCobertura, Defecto);
      (Pedunculo == 0, sin_pedunculo(Pedunculo, Defecto));
      ((FrutoDoble == 1; FrutoDoble == 2), fruto_doble(FrutoDoble, Defecto));
      (PorcentajeCicatridura > 10, determinarCicatridura(PorcentajeCicatridura, Defecto));
      (PorcentajeArrugado > 10, determinarArrugado(PorcentajeArrugado, Defecto)).


%//////////////////////////// ENTRADA //////////////////
%La consulta de entrada es la cereza la cual estará expresada cómo una lista de sus características de la cereza.

% Entrada de prueba:
% cereza(25, medio, abrasion, 50, Coloracion, 20, 20, 1, 0, Salida, NumeroLinea, Defectos).

cereza(Calibre, NivelCobertura, TipoMancha, PorcentajeColoracion, Coloracion, PorcentajeCicatridura, PorcentajeArrugado, Pedunculo, FrutoDoble, Salida, NumeroLinea, Defectos):-
    (calibre(Tamano, Calibre),
    determinarColoracion(PorcentajeColoracion, Coloracion),
    findall(Defecto, detectarDefectos(Coloracion, TipoMancha, NivelCobertura, PorcentajeCicatridura, PorcentajeArrugado, Pedunculo, FrutoDoble, Defecto), Defectos),
    salidaLineaEmbalaje(NumeroLinea, Calibre),
    length(Defectos, C)
    ),
    (
    % Exportable
    ((NivelCobertura == -),
    (Tamano=mediana; Tamano=grande),
    C == 0,
    salida(Salida, 1)
    );
    % Mercado interno
    ((NivelCobertura = bajo ;NivelCobertura=medio; NivelCobertura== -),
    (Tamano=chica; Tamano=mediana; Tamano=grande),
    C < 3,
    salida(Salida, 2));
    % Desecho
    ((NivelCobertura=alto; NivelCobertura=medio; NivelCobertura == -),
    (Tamano=chica; Tamano=mediana; Tamano=grande),
    salida(Salida, 3))
    ),!.














