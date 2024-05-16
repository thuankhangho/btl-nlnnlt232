.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object
.field static a F

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
	ldc 1.0
	putstatic ZCodeClass/a F
	return
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static foo(F)F
Label0:
	ldc 1.0
	freturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static foo1(F)Z
Label0:
	iconst_0
	ireturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args Ljava/lang/String; from Label0 to Label1
	return
Label1:
.limit stack 0
.limit locals 1
.end method
