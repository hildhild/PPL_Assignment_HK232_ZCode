.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

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
	return
Label1:
.limit stack 0
.limit locals 0
.end method

.method public static printMinArray([F)F
Label0:
.var 0 is x [F from Label0 to Label1
.var 1 is for F from Label0 to Label1
Label2:
.var 2 is i Ljava/lang/Object; from Label2 to Label3
	ldc 1.0000
	fstore_2
.var 3 is min Ljava/lang/Object; from Label2 to Label3
	aload_0
	ldc 0.0000
	f2i
	faload
	fstore_3
	fload_2
	fstore_1
Label6:
	fload_2
	ldc 10.0000
	fcmpl
	iflt Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label5
Label9:
	fload_3
	aload_0
	fload_2
	f2i
	faload
	fcmpl
	ifle Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
	aload_0
	fload_2
	f2i
	faload
	fstore_3
Label11:
Label10:
Label4:
	fload_2
	ldc 1.0000
	fadd
	fstore_2
	goto Label6
Label5:
	fload_1
	fstore_2
	fload_3
	freturn
Label3:
Label1:
.limit stack 6
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is for F from Label0 to Label1
Label2:
.var 2 is a Ljava/lang/Object; from Label2 to Label3
	ldc 10.0000
	f2i
	newarray float
	dup
	ldc 0.0000
	f2i
	ldc 1.0000
	fastore
	dup
	ldc 1.0000
	f2i
	ldc 2.0000
	fastore
	dup
	ldc 2.0000
	f2i
	ldc 3.0000
	fastore
	dup
	ldc 3.0000
	f2i
	ldc 4.0000
	fastore
	dup
	ldc 4.0000
	f2i
	ldc 5.0000
	fastore
	dup
	ldc 5.0000
	f2i
	ldc 0.0000
	fastore
	dup
	ldc 6.0000
	f2i
	ldc 7.0000
	fastore
	dup
	ldc 7.0000
	f2i
	ldc 8.0000
	fastore
	dup
	ldc 8.0000
	f2i
	ldc 1.0000
	fneg
	fastore
	dup
	ldc 9.0000
	f2i
	ldc 10.0000
	fastore
	astore_2
.var 3 is c Ljava/lang/Object; from Label2 to Label3
	aload_2
	invokestatic ZCodeClass/printMinArray([F)F
	fstore_3
	fload_3
	invokestatic io/writeNumber(F)V
Label3:
	return
Label1:
.limit stack 5
.limit locals 4
.end method
