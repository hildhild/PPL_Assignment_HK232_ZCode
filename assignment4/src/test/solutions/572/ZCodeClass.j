.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object
.field static a [Z
.field static b [[Z

.method public <init>()V
Label0:
.var 0 is this LZCodeClass; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
	return
Label1:
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
	ldc 2.0000
	f2i
	newarray boolean
	putstatic ZCodeClass.a [Z
	ldc 2.0000
	f2i
	ldc 2.0000
	f2i
	multianewarray [[Z 2
	putstatic ZCodeClass.b [[Z
	return
Label1:
.limit stack 2
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is for F from Label0 to Label1
Label2:
	getstatic ZCodeClass.a [Z
	ldc 1.0000
	f2i
	baload
	invokestatic io/writeBool(Z)V
	getstatic ZCodeClass.b [[Z
	ldc 0.0000
	f2i
	aaload
	ldc 0.0000
	f2i
	baload
	invokestatic io/writeBool(Z)V
	getstatic ZCodeClass.a [Z
	ldc 0.0000
	f2i
	iconst_1
	bastore
	getstatic ZCodeClass.a [Z
	ldc 0.0000
	f2i
	baload
	invokestatic io/writeBool(Z)V
	getstatic ZCodeClass.b [[Z
	ldc 0.0000
	f2i
	aaload
	ldc 0.0000
	f2i
	iconst_1
	bastore
	getstatic ZCodeClass.b [[Z
	ldc 0.0000
	f2i
	aaload
	ldc 0.0000
	f2i
	baload
	invokestatic io/writeBool(Z)V
.var 2 is c Ljava/lang/Object; from Label2 to Label3
	getstatic ZCodeClass.b [[Z
	ldc 0.0000
	f2i
	aaload
	astore_2
	aload_2
	ldc 1.0000
	f2i
	iconst_1
	bastore
	getstatic ZCodeClass.b [[Z
	ldc 0.0000
	f2i
	aaload
	ldc 1.0000
	f2i
	baload
	invokestatic io/writeBool(Z)V
Label3:
	return
Label1:
.limit stack 11
.limit locals 3
.end method
