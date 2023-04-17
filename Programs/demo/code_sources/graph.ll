; ModuleID = 'graph.cc'
source_filename = "graph.cc"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@.str = private unnamed_addr constant [8 x i8] c"funca%d\00", align 1
@.str.1 = private unnamed_addr constant [8 x i8] c"funcb%d\00", align 1
@.str.2 = private unnamed_addr constant [8 x i8] c"funcc%d\00", align 1

; Function Attrs: noinline optnone uwtable mustprogress
define dso_local void @_Z1ai(i32 %0) #0 !dbg !7 {
  %2 = alloca i32, align 4
  store i32 %0, i32* %2, align 4
  call void @llvm.dbg.declare(metadata i32* %2, metadata !11, metadata !DIExpression()), !dbg !12
  %3 = load i32, i32* %2, align 4, !dbg !13
  %4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.str, i64 0, i64 0), i32 %3), !dbg !14
  ret void, !dbg !15
}

; Function Attrs: nofree nosync nounwind readnone speculatable willreturn
declare void @llvm.dbg.declare(metadata, metadata, metadata) #1

declare dso_local i32 @printf(i8*, ...) #2

; Function Attrs: noinline optnone uwtable mustprogress
define dso_local void @_Z1bi(i32 %0) #0 !dbg !16 {
  %2 = alloca i32, align 4
  store i32 %0, i32* %2, align 4
  call void @llvm.dbg.declare(metadata i32* %2, metadata !17, metadata !DIExpression()), !dbg !18
  %3 = load i32, i32* %2, align 4, !dbg !19
  %4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.str.1, i64 0, i64 0), i32 %3), !dbg !20
  ret void, !dbg !21
}

; Function Attrs: noinline optnone uwtable mustprogress
define dso_local void @_Z1ci(i32 %0) #0 !dbg !22 {
  %2 = alloca i32, align 4
  store i32 %0, i32* %2, align 4
  call void @llvm.dbg.declare(metadata i32* %2, metadata !23, metadata !DIExpression()), !dbg !24
  %3 = load i32, i32* %2, align 4, !dbg !25
  %4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.str.2, i64 0, i64 0), i32 %3), !dbg !26
  ret void, !dbg !27
}

; Function Attrs: noinline norecurse optnone uwtable mustprogress
define dso_local i32 @main() #3 !dbg !28 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  call void @llvm.dbg.declare(metadata i32* %2, metadata !31, metadata !DIExpression()), !dbg !32
  store i32 10, i32* %2, align 4, !dbg !32
  %3 = load i32, i32* %2, align 4, !dbg !33
  %4 = icmp sgt i32 %3, 5, !dbg !35
  br i1 %4, label %5, label %7, !dbg !36

5:                                                ; preds = %0
  %6 = load i32, i32* %2, align 4, !dbg !37
  call void @_Z1ai(i32 %6), !dbg !39
  br label %9, !dbg !40

7:                                                ; preds = %0
  %8 = load i32, i32* %2, align 4, !dbg !41
  call void @_Z1bi(i32 %8), !dbg !43
  br label %9

9:                                                ; preds = %7, %5
  %10 = load i32, i32* %2, align 4, !dbg !44
  call void @_Z1ci(i32 %10), !dbg !45
  ret i32 0, !dbg !46
}

attributes #0 = { noinline optnone uwtable mustprogress "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { nofree nosync nounwind readnone speculatable willreturn }
attributes #2 = { "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { noinline norecurse optnone uwtable mustprogress "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.dbg.cu = !{!0}
!llvm.module.flags = !{!3, !4, !5}
!llvm.ident = !{!6}

!0 = distinct !DICompileUnit(language: DW_LANG_C_plus_plus_14, file: !1, producer: "clang version 12.0.1 (git@github.com:fengzhengzhan/STFGFuzz.git 4ed35f2f97b6ad76c9de46553c4fdd545c0c1eb2)", isOptimized: false, runtimeVersion: 0, emissionKind: FullDebug, enums: !2, splitDebugInlining: false, nameTableKind: None)
!1 = !DIFile(filename: "graph.cc", directory: "/home/fzz/Desktop/STFGFuzz/Programs/demo/code_sources")
!2 = !{}
!3 = !{i32 7, !"Dwarf Version", i32 4}
!4 = !{i32 2, !"Debug Info Version", i32 3}
!5 = !{i32 1, !"wchar_size", i32 4}
!6 = !{!"clang version 12.0.1 (git@github.com:fengzhengzhan/STFGFuzz.git 4ed35f2f97b6ad76c9de46553c4fdd545c0c1eb2)"}
!7 = distinct !DISubprogram(name: "a", linkageName: "_Z1ai", scope: !1, file: !1, line: 3, type: !8, scopeLine: 3, flags: DIFlagPrototyped, spFlags: DISPFlagDefinition, unit: !0, retainedNodes: !2)
!8 = !DISubroutineType(types: !9)
!9 = !{null, !10}
!10 = !DIBasicType(name: "int", size: 32, encoding: DW_ATE_signed)
!11 = !DILocalVariable(name: "x", arg: 1, scope: !7, file: !1, line: 3, type: !10)
!12 = !DILocation(line: 3, column: 12, scope: !7)
!13 = !DILocation(line: 4, column: 23, scope: !7)
!14 = !DILocation(line: 4, column: 5, scope: !7)
!15 = !DILocation(line: 5, column: 1, scope: !7)
!16 = distinct !DISubprogram(name: "b", linkageName: "_Z1bi", scope: !1, file: !1, line: 7, type: !8, scopeLine: 7, flags: DIFlagPrototyped, spFlags: DISPFlagDefinition, unit: !0, retainedNodes: !2)
!17 = !DILocalVariable(name: "x", arg: 1, scope: !16, file: !1, line: 7, type: !10)
!18 = !DILocation(line: 7, column: 12, scope: !16)
!19 = !DILocation(line: 8, column: 23, scope: !16)
!20 = !DILocation(line: 8, column: 5, scope: !16)
!21 = !DILocation(line: 9, column: 1, scope: !16)
!22 = distinct !DISubprogram(name: "c", linkageName: "_Z1ci", scope: !1, file: !1, line: 11, type: !8, scopeLine: 11, flags: DIFlagPrototyped, spFlags: DISPFlagDefinition, unit: !0, retainedNodes: !2)
!23 = !DILocalVariable(name: "x", arg: 1, scope: !22, file: !1, line: 11, type: !10)
!24 = !DILocation(line: 11, column: 12, scope: !22)
!25 = !DILocation(line: 12, column: 23, scope: !22)
!26 = !DILocation(line: 12, column: 5, scope: !22)
!27 = !DILocation(line: 13, column: 1, scope: !22)
!28 = distinct !DISubprogram(name: "main", scope: !1, file: !1, line: 15, type: !29, scopeLine: 15, flags: DIFlagPrototyped, spFlags: DISPFlagDefinition, unit: !0, retainedNodes: !2)
!29 = !DISubroutineType(types: !30)
!30 = !{!10}
!31 = !DILocalVariable(name: "x", scope: !28, file: !1, line: 16, type: !10)
!32 = !DILocation(line: 16, column: 9, scope: !28)
!33 = !DILocation(line: 17, column: 9, scope: !34)
!34 = distinct !DILexicalBlock(scope: !28, file: !1, line: 17, column: 9)
!35 = !DILocation(line: 17, column: 11, scope: !34)
!36 = !DILocation(line: 17, column: 9, scope: !28)
!37 = !DILocation(line: 18, column: 11, scope: !38)
!38 = distinct !DILexicalBlock(scope: !34, file: !1, line: 17, column: 16)
!39 = !DILocation(line: 18, column: 9, scope: !38)
!40 = !DILocation(line: 19, column: 5, scope: !38)
!41 = !DILocation(line: 20, column: 11, scope: !42)
!42 = distinct !DILexicalBlock(scope: !34, file: !1, line: 19, column: 12)
!43 = !DILocation(line: 20, column: 9, scope: !42)
!44 = !DILocation(line: 22, column: 7, scope: !28)
!45 = !DILocation(line: 22, column: 5, scope: !28)
!46 = !DILocation(line: 23, column: 5, scope: !28)
