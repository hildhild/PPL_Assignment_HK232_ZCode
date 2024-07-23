.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object
.field static b [Ljava/lang/String;

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
	ldc 1.0000
	f2i
	anewarray java/lang/String
	dup
	ldc 0.0000
	f2i
	ldc "tien"
	aastore
	putstatic ZCodeClass.b [Ljava/lang/String;
	return
Label1:
.limit stack 5
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is for F from Label0 to Label1
Label2:
.var 2 is a Ljava/lang/Object; from Label2 to Label3
	ldc 2.0000
	f2i
	anewarray [Ljava/lang/String;
	dup
	ldc 0.0000
	f2i
	ldc 1.0000
	f2i
	anewarray java/lang/String
	dup
	ldc 0.0000
	f2i
	ldc "v"
	aastore
	aastore
	dup
	ldc 1.0000
	f2i
	ldc 1.0000
	f2i
	anewarray java/lang/String
	dup
	ldc 0.0000
	f2i
	ldc "o"
	aastore
	aastore
	astore_2
	aload_2
	ldc 1.0000
	f2i
	aaload
	ldc 0.0000
	f2i
	aaload
	invokestatic io/writeString(Ljava/lang/String;)V
	aload_2
	ldc 0.0000
	f2i
	aaload
	ldc 0.0000
	f2i
	aaload
	invokestatic io/writeString(Ljava/lang/String;)V
	getstatic ZCodeClass.b [Ljava/lang/String;
	ldc 0.0000
	f2i
	aaload
	invokestatic io/writeString(Ljava/lang/String;)V
Label3:
	return
Label1:
.limit stack 10
.limit locals 3
.end method
