; ModuleID = 'IR/demo.ll'
source_filename = "demo/demo.cc"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

%"class.std::ios_base::Init" = type { i8 }
%struct.option = type { i8*, i32, i32*, i32 }
%struct._IO_FILE = type { i32, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, i8*, %struct._IO_marker*, %struct._IO_FILE*, i32, i32, i64, i16, i8, [1 x i8], i8*, i64, %struct._IO_codecvt*, %struct._IO_wide_data*, %struct._IO_FILE*, i8*, i64, i32, [20 x i8] }
%struct._IO_marker = type opaque
%struct._IO_codecvt = type opaque
%struct._IO_wide_data = type opaque

$"__cxx_global_var_init$21576b91ab9b15712202e1b4a494877f" = comdat any

$main = comdat any

$"_GLOBAL__sub_I_demo.cc$21576b91ab9b15712202e1b4a494877f" = comdat any

$sancov.module_ctor_trace_pc_guard = comdat any

@_ZStL8__ioinit = internal global { %"class.std::ios_base::Init", [63 x i8] } zeroinitializer, align 32
@__dso_handle = external hidden global i8
@_ZZ4mainE12long_options = internal global { [1 x %struct.option], [32 x i8] } { [1 x %struct.option] [%struct.option { i8* getelementptr inbounds ({ [5 x i8], [59 x i8] }, { [5 x i8], [59 x i8] }* @.str, i32 0, i32 0, i32 0), i32 1, i32* null, i32 102 }], [32 x i8] zeroinitializer }, align 32
@.str = internal constant { [5 x i8], [59 x i8] } { [5 x i8] c"file\00", [59 x i8] zeroinitializer }, align 32
@.str.1 = internal constant { [3 x i8], [61 x i8] } { [3 x i8] c"f:\00", [61 x i8] zeroinitializer }, align 32
@optarg = external dso_local global i8*, align 8
@.str.2 = internal constant { [18 x i8], [46 x i8] } { [18 x i8] c"Error Parameters!\00", [46 x i8] zeroinitializer }, align 32
@.str.3 = internal constant { [2 x i8], [62 x i8] } { [2 x i8] c"r\00", [62 x i8] zeroinitializer }, align 32
@.str.4 = internal constant { [27 x i8], [37 x i8] } { [27 x i8] c"---------------------   %c\00", [37 x i8] zeroinitializer }, align 32
@.str.5 = internal constant { [21 x i8], [43 x i8] } { [21 x i8] c"The quick brown fox \00", [43 x i8] zeroinitializer }, align 32
@.str.6 = internal constant { [12 x i8], [52 x i8] } { [12 x i8] c"jumps over \00", [52 x i8] zeroinitializer }, align 32
@.str.7 = internal constant { [14 x i8], [50 x i8] } { [14 x i8] c"the lazy dog.\00", [50 x i8] zeroinitializer }, align 32
@.str.8 = internal constant { [27 x i8], [37 x i8] } { [27 x i8] c"Though first str/mem Cmp.\0A\00", [37 x i8] zeroinitializer }, align 32
@.str.9 = internal constant { [4 x i8], [60 x i8] } { [4 x i8] c"%s\0A\00", [60 x i8] zeroinitializer }, align 32
@.str.10 = internal constant { [33 x i8], [63 x i8] } { [33 x i8] c"Puzzle solved, Congratulations!\0A\00", [63 x i8] zeroinitializer }, align 32
@__sancov_lowest_stack = external thread_local(initialexec) global i64
@__sancov_gen_ = private global [1 x i32] zeroinitializer, section "__sancov_guards", comdat($"__cxx_global_var_init$21576b91ab9b15712202e1b4a494877f"), align 4, !associated !0
@__sancov_gen_.11 = private global [13 x i32] zeroinitializer, section "__sancov_guards", comdat($main), align 4, !associated !1
@__sancov_gen_cov_switch_values = internal global [3 x i64] [i64 1, i64 32, i64 102]
@__sancov_gen_cov_switch_values.12 = internal global [3 x i64] [i64 1, i64 32, i64 48879]
@__sancov_gen_.13 = private global [1 x i32] zeroinitializer, section "__sancov_guards", comdat($"_GLOBAL__sub_I_demo.cc$21576b91ab9b15712202e1b4a494877f"), align 4, !associated !2
@__start___sancov_guards = external hidden global i32
@__stop___sancov_guards = external hidden global i32
@__asan_option_detect_stack_use_after_return = external global i32
@___asan_gen_ = private unnamed_addr constant [87 x i8] c"6 32 4 9 opt_index 48 201 3 str 320 45 6 buffer 400 201 2 s1 672 201 2 s2 944 201 2 s3\00", align 1
@___asan_gen_.14 = private constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.15 = private unnamed_addr constant [14 x i8] c"std::__ioinit\00", align 1
@___asan_gen_.16 = private unnamed_addr constant [67 x i8] c"/usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/iostream\00", align 1
@___asan_gen_.17 = private unnamed_addr constant { [67 x i8]*, i32, i32 } { [67 x i8]* @___asan_gen_.16, i32 74, i32 25 }
@___asan_gen_.18 = private unnamed_addr constant [13 x i8] c"long_options\00", align 1
@___asan_gen_.19 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.20 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.19, i32 18, i32 26 }
@___asan_gen_.21 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.22 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.23 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.22, i32 20, i32 10 }
@___asan_gen_.24 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.25 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.26 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.25, i32 22, i32 42 }
@___asan_gen_.27 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.28 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.29 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.28, i32 31, i32 20 }
@___asan_gen_.30 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.31 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.32 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.31, i32 39, i32 32 }
@___asan_gen_.33 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.34 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.35 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.34, i32 46, i32 12 }
@___asan_gen_.36 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.37 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.38 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.37, i32 52, i32 28 }
@___asan_gen_.39 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.40 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.41 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.40, i32 53, i32 30 }
@___asan_gen_.42 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.43 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.44 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.43, i32 54, i32 29 }
@___asan_gen_.45 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.46 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.47 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.46, i32 58, i32 12 }
@___asan_gen_.48 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.49 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.50 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.49, i32 73, i32 12 }
@___asan_gen_.51 = private unnamed_addr constant [17 x i8] c"<string literal>\00", align 1
@___asan_gen_.52 = private unnamed_addr constant [13 x i8] c"demo/demo.cc\00", align 1
@___asan_gen_.53 = private unnamed_addr constant { [13 x i8]*, i32, i32 } { [13 x i8]* @___asan_gen_.52, i32 95, i32 12 }
@llvm.compiler.used = appending global [16 x i8*] [i8* bitcast ([1 x i32]* @__sancov_gen_ to i8*), i8* bitcast ([13 x i32]* @__sancov_gen_.11 to i8*), i8* bitcast ([1 x i32]* @__sancov_gen_.13 to i8*), i8* getelementptr inbounds ({ %"class.std::ios_base::Init", [63 x i8] }, { %"class.std::ios_base::Init", [63 x i8] }* @_ZStL8__ioinit, i32 0, i32 0, i32 0), i8* bitcast ({ [1 x %struct.option], [32 x i8] }* @_ZZ4mainE12long_options to i8*), i8* getelementptr inbounds ({ [5 x i8], [59 x i8] }, { [5 x i8], [59 x i8] }* @.str, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [3 x i8], [61 x i8] }, { [3 x i8], [61 x i8] }* @.str.1, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [18 x i8], [46 x i8] }, { [18 x i8], [46 x i8] }* @.str.2, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [2 x i8], [62 x i8] }, { [2 x i8], [62 x i8] }* @.str.3, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [27 x i8], [37 x i8] }, { [27 x i8], [37 x i8] }* @.str.4, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [21 x i8], [43 x i8] }, { [21 x i8], [43 x i8] }* @.str.5, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [12 x i8], [52 x i8] }, { [12 x i8], [52 x i8] }* @.str.6, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [14 x i8], [50 x i8] }, { [14 x i8], [50 x i8] }* @.str.7, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [27 x i8], [37 x i8] }, { [27 x i8], [37 x i8] }* @.str.8, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [4 x i8], [60 x i8] }, { [4 x i8], [60 x i8] }* @.str.9, i32 0, i32 0, i32 0), i8* getelementptr inbounds ({ [33 x i8], [63 x i8] }, { [33 x i8], [63 x i8] }* @.str.10, i32 0, i32 0, i32 0)], section "llvm.metadata"
@0 = internal global [13 x { i64, i64, i64, i64, i64, i64, i64, i64 }] [{ i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ %"class.std::ios_base::Init", [63 x i8] }* @_ZStL8__ioinit to i64), i64 1, i64 64, i64 ptrtoint ([14 x i8]* @___asan_gen_.15 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.14 to i64), i64 1, i64 ptrtoint ({ [67 x i8]*, i32, i32 }* @___asan_gen_.17 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [1 x %struct.option], [32 x i8] }* @_ZZ4mainE12long_options to i64), i64 32, i64 64, i64 ptrtoint ([13 x i8]* @___asan_gen_.18 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.14 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.20 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [5 x i8], [59 x i8] }* @.str to i64), i64 5, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.21 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.14 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.23 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [3 x i8], [61 x i8] }* @.str.1 to i64), i64 3, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.24 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.14 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.26 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [18 x i8], [46 x i8] }* @.str.2 to i64), i64 18, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.27 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.14 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.29 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [2 x i8], [62 x i8] }* @.str.3 to i64), i64 2, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.30 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.14 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.32 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [27 x i8], [37 x i8] }* @.str.4 to i64), i64 27, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.33 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.14 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.35 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [21 x i8], [43 x i8] }* @.str.5 to i64), i64 21, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.36 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.14 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.38 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [12 x i8], [52 x i8] }* @.str.6 to i64), i64 12, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.39 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.14 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.41 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [14 x i8], [50 x i8] }* @.str.7 to i64), i64 14, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.42 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.14 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.44 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [27 x i8], [37 x i8] }* @.str.8 to i64), i64 27, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.45 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.14 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.47 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [4 x i8], [60 x i8] }* @.str.9 to i64), i64 4, i64 64, i64 ptrtoint ([17 x i8]* @___asan_gen_.48 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.14 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.50 to i64), i64 -1 }, { i64, i64, i64, i64, i64, i64, i64, i64 } { i64 ptrtoint ({ [33 x i8], [63 x i8] }* @.str.10 to i64), i64 33, i64 96, i64 ptrtoint ([17 x i8]* @___asan_gen_.51 to i64), i64 ptrtoint ([13 x i8]* @___asan_gen_.14 to i64), i64 0, i64 ptrtoint ({ [13 x i8]*, i32, i32 }* @___asan_gen_.53 to i64), i64 -1 }]
@llvm.global_ctors = appending global [3 x { i32, void ()*, i8* }] [{ i32, void ()*, i8* } { i32 65535, void ()* @_GLOBAL__sub_I_demo.cc, i8* null }, { i32, void ()*, i8* } { i32 2, void ()* @sancov.module_ctor_trace_pc_guard, i8* bitcast (void ()* @sancov.module_ctor_trace_pc_guard to i8*) }, { i32, void ()*, i8* } { i32 1, void ()* @asan.module_ctor, i8* null }]
@llvm.global_dtors = appending global [1 x { i32, void ()*, i8* }] [{ i32, void ()*, i8* } { i32 1, void ()* @asan.module_dtor, i8* null }]

; Function Attrs: noinline sanitize_address uwtable
define internal void @__cxx_global_var_init() #0 section ".text.startup" comdat($"__cxx_global_var_init$21576b91ab9b15712202e1b4a494877f") {
entry:
  call void @__sanitizer_cov_trace_pc_guard(i32* getelementptr inbounds ([1 x i32], [1 x i32]* @__sancov_gen_, i32 0, i32 0)) #8
  call void @_ZNSt8ios_base4InitC1Ev(%"class.std::ios_base::Init"* nonnull dereferenceable(1) getelementptr inbounds ({ %"class.std::ios_base::Init", [63 x i8] }, { %"class.std::ios_base::Init", [63 x i8] }* @_ZStL8__ioinit, i32 0, i32 0))
  br label %0

0:                                                ; preds = %entry
  %1 = call i32 @__cxa_atexit(void (i8*)* bitcast (void (%"class.std::ios_base::Init"*)* @_ZNSt8ios_base4InitD1Ev to void (i8*)*), i8* getelementptr inbounds ({ %"class.std::ios_base::Init", [63 x i8] }, { %"class.std::ios_base::Init", [63 x i8] }* @_ZStL8__ioinit, i32 0, i32 0, i32 0), i8* @__dso_handle) #3
  ret void
}

declare dso_local void @_ZNSt8ios_base4InitC1Ev(%"class.std::ios_base::Init"* nonnull dereferenceable(1)) unnamed_addr #1

; Function Attrs: nounwind
declare dso_local void @_ZNSt8ios_base4InitD1Ev(%"class.std::ios_base::Init"* nonnull dereferenceable(1)) unnamed_addr #2

; Function Attrs: nounwind
declare dso_local i32 @__cxa_atexit(void (i8*)*, i8*, i8*) #3

; Function Attrs: noinline norecurse optnone sanitize_address uwtable mustprogress
define dso_local i32 @main(i32 %argc, i8** %argv) #4 comdat {
entry:
  %retval = alloca i32, align 4
  %argc.addr = alloca i32, align 4
  %argv.addr = alloca i8**, align 8
  %opt = alloca i32, align 4
  %filename = alloca i8*, align 8
  %fp = alloca %struct._IO_FILE*, align 8
  %cleanup.dest.slot = alloca i32, align 4
  %i = alloca i32, align 4
  %i24 = alloca i32, align 4
  br label %0

0:                                                ; preds = %entry
  %i39 = alloca i32, align 4
  %x = alloca i64, align 8
  %y = alloca i32, align 4
  %z = alloca i16, align 2
  %asan_local_stack_base = alloca i64, align 8
  %1 = load i32, i32* @__asan_option_detect_stack_use_after_return, align 4
  %2 = icmp ne i32 %1, 0
  br i1 %2, label %3, label %6

3:                                                ; preds = %0
  %4 = call i64 @__asan_stack_malloc_5(i64 1216)
  br label %5

5:                                                ; preds = %3
  br label %6

6:                                                ; preds = %5, %0
  %7 = phi i64 [ 0, %0 ], [ %4, %5 ]
  %8 = icmp eq i64 %7, 0
  br i1 %8, label %9, label %12

9:                                                ; preds = %6
  %MyAlloca = alloca i8, i64 1216, align 32
  %10 = ptrtoint i8* %MyAlloca to i64
  br label %11

11:                                               ; preds = %9
  br label %12

12:                                               ; preds = %11, %6
  %13 = phi i64 [ %7, %6 ], [ %10, %11 ]
  store i64 %13, i64* %asan_local_stack_base, align 8
  %14 = add i64 %13, 32
  %15 = inttoptr i64 %14 to i32*
  %16 = add i64 %13, 48
  %17 = inttoptr i64 %16 to [201 x i8]*
  %18 = add i64 %13, 320
  %19 = inttoptr i64 %18 to [45 x i8]*
  %20 = add i64 %13, 400
  %21 = inttoptr i64 %20 to [201 x i8]*
  %22 = add i64 %13, 672
  %23 = inttoptr i64 %22 to [201 x i8]*
  %24 = add i64 %13, 944
  %25 = inttoptr i64 %24 to [201 x i8]*
  %26 = inttoptr i64 %13 to i64*
  store i64 1102416563, i64* %26, align 8
  %27 = add i64 %13, 8
  %28 = inttoptr i64 %27 to i64*
  store i64 ptrtoint ([87 x i8]* @___asan_gen_ to i64), i64* %28, align 8
  %29 = add i64 %13, 16
  %30 = inttoptr i64 %29 to i64*
  store i64 ptrtoint (i32 (i32, i8**)* @main to i64), i64* %30, align 8
  %31 = lshr i64 %13, 3
  %32 = add i64 %31, 2147450880
  %33 = add i64 %32, 0
  %34 = inttoptr i64 %33 to i64*
  store i64 -506387807054204431, i64* %34, align 1
  %35 = add i64 %32, 8
  %36 = inttoptr i64 %35 to i64*
  store i64 -506381209866536712, i64* %36, align 1
  %37 = add i64 %32, 16
  %38 = inttoptr i64 %37 to i64*
  store i64 -506381209866536712, i64* %38, align 1
  %39 = add i64 %32, 24
  %40 = inttoptr i64 %39 to i64*
  store i64 -506381209866536712, i64* %40, align 1
  %41 = add i64 %32, 32
  %42 = inttoptr i64 %41 to i64*
  store i64 -940422246894996750, i64* %42, align 1
  %43 = add i64 %32, 40
  %44 = inttoptr i64 %43 to i64*
  store i64 -940415623954368264, i64* %44, align 1
  %45 = add i64 %32, 48
  %46 = inttoptr i64 %45 to i64*
  store i64 -506381209866538254, i64* %46, align 1
  %47 = add i64 %32, 56
  %48 = inttoptr i64 %47 to i64*
  store i64 -506381209866536712, i64* %48, align 1
  %49 = add i64 %32, 64
  %50 = inttoptr i64 %49 to i64*
  store i64 -506381209866536712, i64* %50, align 1
  %51 = add i64 %32, 72
  %52 = inttoptr i64 %51 to i64*
  store i64 -940422246793938696, i64* %52, align 1
  %53 = add i64 %32, 80
  %54 = inttoptr i64 %53 to i64*
  store i64 -506381209967594766, i64* %54, align 1
  %55 = add i64 %32, 88
  %56 = inttoptr i64 %55 to i64*
  store i64 -506381209866536712, i64* %56, align 1
  %57 = add i64 %32, 96
  %58 = inttoptr i64 %57 to i64*
  store i64 -506381209866536712, i64* %58, align 1
  %59 = add i64 %32, 104
  %60 = inttoptr i64 %59 to i64*
  store i64 -940415623954368264, i64* %60, align 1
  %61 = add i64 %32, 112
  %62 = inttoptr i64 %61 to i64*
  store i64 -506387832807165198, i64* %62, align 1
  %63 = add i64 %32, 120
  %64 = inttoptr i64 %63 to i64*
  store i64 -506381209866536712, i64* %64, align 1
  %65 = add i64 %32, 128
  %66 = inttoptr i64 %65 to i64*
  store i64 -506381209866536712, i64* %66, align 1
  %67 = add i64 %32, 136
  %68 = inttoptr i64 %67 to i64*
  store i64 -506381209866536712, i64* %68, align 1
  %69 = add i64 %32, 144
  %70 = inttoptr i64 %69 to i64*
  store i64 -868082074056920077, i64* %70, align 1
  call void @__sanitizer_cov_trace_pc_guard(i32* getelementptr inbounds ([13 x i32], [13 x i32]* @__sancov_gen_.11, i32 0, i32 0)) #8
  store i32 0, i32* %retval, align 4
  store i32 %argc, i32* %argc.addr, align 4
  store i8** %argv, i8*** %argv.addr, align 8
  %71 = bitcast i32* %opt to i8*
  call void @llvm.lifetime.start.p0i8(i64 4, i8* %71) #3
  %72 = bitcast i32* %15 to i8*
  %73 = add i64 %32, 4
  %74 = inttoptr i64 %73 to i8*
  store i8 4, i8* %74, align 1
  call void @llvm.lifetime.start.p0i8(i64 4, i8* %72) #3
  %75 = bitcast i8** %filename to i8*
  call void @llvm.lifetime.start.p0i8(i64 8, i8* %75) #3
  br label %while.cond

while.cond:                                       ; preds = %sw.epilog, %12
  %76 = load i32, i32* %argc.addr, align 4
  %77 = load i8**, i8*** %argv.addr, align 8
  %call = call i32 @getopt_long(i32 %76, i8** %77, i8* getelementptr inbounds ({ [3 x i8], [61 x i8] }, { [3 x i8], [61 x i8] }* @.str.1, i32 0, i32 0, i64 0), %struct.option* getelementptr inbounds ({ [1 x %struct.option], [32 x i8] }, { [1 x %struct.option], [32 x i8] }* @_ZZ4mainE12long_options, i32 0, i32 0, i64 0), i32* %15) #3
  store i32 %call, i32* %opt, align 4
  br label %78

78:                                               ; preds = %while.cond
  call void @__sanitizer_cov_trace_const_cmp4(i32 -1, i32 %call)
  %cmp = icmp ne i32 %call, -1
  br i1 %cmp, label %while.body, label %while.end

while.body:                                       ; preds = %78
  %79 = load i32, i32* %opt, align 4
  %80 = zext i32 %79 to i64
  br label %81

81:                                               ; preds = %while.body
  call void @__sanitizer_cov_trace_switch(i64 %80, i64* getelementptr inbounds ([3 x i64], [3 x i64]* @__sancov_gen_cov_switch_values, i32 0, i32 0))
  switch i32 %79, label %sw.default [
    i32 102, label %sw.bb
  ]

sw.bb:                                            ; preds = %81
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([13 x i32]* @__sancov_gen_.11 to i64), i64 4) to i32*)) #8
  %82 = load i8, i8* inttoptr (i64 add (i64 lshr (i64 ptrtoint (i8** @optarg to i64), i64 3), i64 2147450880) to i8*), align 1
  br label %83

83:                                               ; preds = %sw.bb
  %84 = icmp ne i8 %82, 0
  br i1 %84, label %85, label %87

85:                                               ; preds = %83
  call void @__asan_report_load8(i64 ptrtoint (i8** @optarg to i64)) #8
  br label %86

86:                                               ; preds = %85
  unreachable

87:                                               ; preds = %83
  %88 = load i8*, i8** @optarg, align 8
  store i8* %88, i8** %filename, align 8
  br label %89

89:                                               ; preds = %87
  br label %sw.epilog

sw.default:                                       ; preds = %81
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([13 x i32]* @__sancov_gen_.11 to i64), i64 8) to i32*)) #8
  %call1 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ({ [18 x i8], [46 x i8] }, { [18 x i8], [46 x i8] }* @.str.2, i32 0, i32 0, i64 0))
  br label %90

90:                                               ; preds = %sw.default
  br label %sw.epilog

sw.epilog:                                        ; preds = %90, %89
  br label %while.cond, !llvm.loop !31

while.end:                                        ; preds = %78
  %91 = bitcast [201 x i8]* %17 to i8*
  %92 = add i64 %32, 6
  %93 = inttoptr i64 %92 to i64*
  store i64 0, i64* %93, align 1
  %94 = add i64 %32, 14
  %95 = inttoptr i64 %94 to i64*
  store i64 0, i64* %95, align 1
  %96 = add i64 %32, 22
  %97 = inttoptr i64 %96 to i64*
  store i64 0, i64* %97, align 1
  %98 = add i64 %32, 30
  %99 = inttoptr i64 %98 to i16*
  store i16 256, i16* %99, align 1
  call void @llvm.lifetime.start.p0i8(i64 201, i8* %91) #3
  %100 = bitcast %struct._IO_FILE** %fp to i8*
  call void @llvm.lifetime.start.p0i8(i64 8, i8* %100) #3
  %101 = load i8*, i8** %filename, align 8
  %call2 = call %struct._IO_FILE* @fopen(i8* %101, i8* getelementptr inbounds ({ [2 x i8], [62 x i8] }, { [2 x i8], [62 x i8] }* @.str.3, i32 0, i32 0, i64 0))
  store %struct._IO_FILE* %call2, %struct._IO_FILE** %fp, align 8
  %arraydecay = getelementptr inbounds [201 x i8], [201 x i8]* %17, i64 0, i64 0
  %102 = load %struct._IO_FILE*, %struct._IO_FILE** %fp, align 8
  %call3 = call i8* @fgets(i8* %arraydecay, i32 201, %struct._IO_FILE* %102)
  br label %103

103:                                              ; preds = %while.end
  %104 = bitcast [45 x i8]* %19 to i8*
  %105 = add i64 %32, 40
  %106 = inttoptr i64 %105 to i32*
  store i32 0, i32* %106, align 1
  %107 = add i64 %32, 44
  %108 = inttoptr i64 %107 to i16*
  store i16 1280, i16* %108, align 1
  call void @llvm.lifetime.start.p0i8(i64 45, i8* %104) #3
  %109 = bitcast [45 x i8]* %19 to i8*
  %110 = call i8* @__asan_memset(i8* %109, i32 0, i64 45)
  %arraydecay4 = getelementptr inbounds [45 x i8], [45 x i8]* %19, i64 0, i64 0
  %arraydecay5 = getelementptr inbounds [201 x i8], [201 x i8]* %17, i64 0, i64 0
  %111 = call i8* @__asan_memcpy(i8* %arraydecay4, i8* %arraydecay5, i64 44)
  %arrayidx = getelementptr inbounds [45 x i8], [45 x i8]* %19, i64 0, i64 44
  %112 = ptrtoint i8* %arrayidx to i64
  %113 = lshr i64 %112, 3
  %114 = add i64 %113, 2147450880
  %115 = inttoptr i64 %114 to i8*
  %116 = load i8, i8* %115, align 1
  %117 = icmp ne i8 %116, 0
  br i1 %117, label %118, label %125, !prof !33

118:                                              ; preds = %103
  %119 = and i64 %112, 7
  %120 = trunc i64 %119 to i8
  br label %121

121:                                              ; preds = %118
  %122 = icmp sge i8 %120, %116
  br i1 %122, label %123, label %125

123:                                              ; preds = %121
  call void @__asan_report_load1(i64 %112) #8
  br label %124

124:                                              ; preds = %123
  unreachable

125:                                              ; preds = %121, %103
  %126 = load i8, i8* %arrayidx, align 4
  %conv = sext i8 %126 to i32
  %call6 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ({ [27 x i8], [37 x i8] }, { [27 x i8], [37 x i8] }* @.str.4, i32 0, i32 0, i64 0), i32 %conv)
  %arrayidx7 = getelementptr inbounds [45 x i8], [45 x i8]* %19, i64 0, i64 44
  %127 = ptrtoint i8* %arrayidx7 to i64
  %128 = lshr i64 %127, 3
  br label %129

129:                                              ; preds = %125
  %130 = add i64 %128, 2147450880
  %131 = inttoptr i64 %130 to i8*
  %132 = load i8, i8* %131, align 1
  %133 = icmp ne i8 %132, 0
  br i1 %133, label %134, label %141, !prof !33

134:                                              ; preds = %129
  %135 = and i64 %127, 7
  %136 = trunc i64 %135 to i8
  br label %137

137:                                              ; preds = %134
  %138 = icmp sge i8 %136, %132
  br i1 %138, label %139, label %141

139:                                              ; preds = %137
  call void @__asan_report_store1(i64 %127) #8
  br label %140

140:                                              ; preds = %139
  unreachable

141:                                              ; preds = %137, %129
  store i8 0, i8* %arrayidx7, align 4
  %arrayidx8 = getelementptr inbounds [45 x i8], [45 x i8]* %19, i64 0, i64 0
  %call9 = call i32 @memcmp(i8* %arrayidx8, i8* getelementptr inbounds ({ [21 x i8], [43 x i8] }, { [21 x i8], [43 x i8] }* @.str.5, i32 0, i32 0, i64 0), i64 20) #9
  br label %142

142:                                              ; preds = %141
  call void @__sanitizer_cov_trace_const_cmp4(i32 0, i32 %call9)
  %cmp10 = icmp ne i32 %call9, 0
  br i1 %cmp10, label %while.end.if.then_crit_edge, label %lor.lhs.false

while.end.if.then_crit_edge:                      ; preds = %142
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([13 x i32]* @__sancov_gen_.11 to i64), i64 12) to i32*)) #8
  br label %143

143:                                              ; preds = %while.end.if.then_crit_edge
  br label %if.then

lor.lhs.false:                                    ; preds = %142
  %arrayidx11 = getelementptr inbounds [45 x i8], [45 x i8]* %19, i64 0, i64 20
  %call12 = call i32 @strncmp(i8* %arrayidx11, i8* getelementptr inbounds ({ [12 x i8], [52 x i8] }, { [12 x i8], [52 x i8] }* @.str.6, i32 0, i32 0, i64 0), i64 11) #10
  call void @__sanitizer_cov_trace_const_cmp4(i32 0, i32 %call12)
  br label %144

144:                                              ; preds = %lor.lhs.false
  %cmp13 = icmp ne i32 %call12, 0
  br i1 %cmp13, label %lor.lhs.false.if.then_crit_edge, label %lor.lhs.false14

lor.lhs.false.if.then_crit_edge:                  ; preds = %144
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([13 x i32]* @__sancov_gen_.11 to i64), i64 16) to i32*)) #8
  br label %145

145:                                              ; preds = %lor.lhs.false.if.then_crit_edge
  br label %if.then

lor.lhs.false14:                                  ; preds = %144
  %arrayidx15 = getelementptr inbounds [45 x i8], [45 x i8]* %19, i64 0, i64 31
  %call16 = call i32 @strcmp(i8* %arrayidx15, i8* getelementptr inbounds ({ [14 x i8], [50 x i8] }, { [14 x i8], [50 x i8] }* @.str.7, i32 0, i32 0, i64 0)) #9
  call void @__sanitizer_cov_trace_const_cmp4(i32 0, i32 %call16)
  br label %146

146:                                              ; preds = %lor.lhs.false14
  %cmp17 = icmp ne i32 %call16, 0
  br i1 %cmp17, label %lor.lhs.false14.if.then_crit_edge, label %if.end

lor.lhs.false14.if.then_crit_edge:                ; preds = %146
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([13 x i32]* @__sancov_gen_.11 to i64), i64 20) to i32*)) #8
  br label %147

147:                                              ; preds = %lor.lhs.false14.if.then_crit_edge
  br label %if.then

if.then:                                          ; preds = %147, %145, %143
  store i32 1, i32* %retval, align 4
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %148

148:                                              ; preds = %if.then
  br label %cleanup81

if.end:                                           ; preds = %146
  %call18 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ({ [27 x i8], [37 x i8] }, { [27 x i8], [37 x i8] }* @.str.8, i32 0, i32 0, i64 0))
  %149 = bitcast [201 x i8]* %21 to i8*
  %150 = add i64 %32, 50
  %151 = inttoptr i64 %150 to i64*
  store i64 0, i64* %151, align 1
  %152 = add i64 %32, 58
  %153 = inttoptr i64 %152 to i64*
  store i64 0, i64* %153, align 1
  %154 = add i64 %32, 66
  %155 = inttoptr i64 %154 to i64*
  store i64 0, i64* %155, align 1
  %156 = add i64 %32, 74
  %157 = inttoptr i64 %156 to i16*
  store i16 256, i16* %157, align 1
  call void @llvm.lifetime.start.p0i8(i64 201, i8* %149) #3
  %158 = bitcast [201 x i8]* %23 to i8*
  %159 = add i64 %32, 84
  %160 = inttoptr i64 %159 to i64*
  store i64 0, i64* %160, align 1
  %161 = add i64 %32, 92
  %162 = inttoptr i64 %161 to i64*
  store i64 0, i64* %162, align 1
  %163 = add i64 %32, 100
  %164 = inttoptr i64 %163 to i64*
  br label %165

165:                                              ; preds = %if.end
  store i64 0, i64* %164, align 1
  %166 = add i64 %32, 108
  %167 = inttoptr i64 %166 to i16*
  store i16 256, i16* %167, align 1
  call void @llvm.lifetime.start.p0i8(i64 201, i8* %158) #3
  %168 = bitcast [201 x i8]* %25 to i8*
  %169 = add i64 %32, 118
  %170 = inttoptr i64 %169 to i64*
  store i64 0, i64* %170, align 1
  %171 = add i64 %32, 126
  %172 = inttoptr i64 %171 to i64*
  store i64 0, i64* %172, align 1
  %173 = add i64 %32, 134
  %174 = inttoptr i64 %173 to i64*
  store i64 0, i64* %174, align 1
  %175 = add i64 %32, 142
  %176 = inttoptr i64 %175 to i16*
  store i16 256, i16* %176, align 1
  call void @llvm.lifetime.start.p0i8(i64 201, i8* %168) #3
  %177 = bitcast i32* %i to i8*
  call void @llvm.lifetime.start.p0i8(i64 4, i8* %177) #3
  store i32 0, i32* %i, align 4
  br label %for.cond

for.cond:                                         ; preds = %217, %165
  %178 = load i32, i32* %i, align 4
  call void @__sanitizer_cov_trace_const_cmp4(i32 16, i32 %178)
  br label %179

179:                                              ; preds = %for.cond
  %cmp19 = icmp slt i32 %178, 16
  br i1 %cmp19, label %for.body, label %for.cond.cleanup

for.cond.cleanup:                                 ; preds = %179
  store i32 5, i32* %cleanup.dest.slot, align 4
  %180 = bitcast i32* %i to i8*
  br label %181

181:                                              ; preds = %for.cond.cleanup
  call void @llvm.lifetime.end.p0i8(i64 4, i8* %180) #3
  br label %for.end

for.body:                                         ; preds = %179
  %182 = load i32, i32* %i, align 4
  %add = add nsw i32 %182, 44
  %idxprom = sext i32 %add to i64
  %arrayidx20 = getelementptr inbounds [201 x i8], [201 x i8]* %17, i64 0, i64 %idxprom
  %183 = ptrtoint i8* %arrayidx20 to i64
  %184 = lshr i64 %183, 3
  br label %185

185:                                              ; preds = %for.body
  %186 = add i64 %184, 2147450880
  %187 = inttoptr i64 %186 to i8*
  %188 = load i8, i8* %187, align 1
  %189 = icmp ne i8 %188, 0
  br i1 %189, label %190, label %197, !prof !33

190:                                              ; preds = %185
  %191 = and i64 %183, 7
  %192 = trunc i64 %191 to i8
  br label %193

193:                                              ; preds = %190
  %194 = icmp sge i8 %192, %188
  br i1 %194, label %195, label %197

195:                                              ; preds = %193
  call void @__asan_report_load1(i64 %183) #8
  br label %196

196:                                              ; preds = %195
  unreachable

197:                                              ; preds = %193, %185
  %198 = load i8, i8* %arrayidx20, align 1
  %199 = load i32, i32* %i, align 4
  %idxprom21 = sext i32 %199 to i64
  %arrayidx22 = getelementptr inbounds [201 x i8], [201 x i8]* %21, i64 0, i64 %idxprom21
  %200 = ptrtoint i8* %arrayidx22 to i64
  %201 = lshr i64 %200, 3
  br label %202

202:                                              ; preds = %197
  %203 = add i64 %201, 2147450880
  %204 = inttoptr i64 %203 to i8*
  %205 = load i8, i8* %204, align 1
  %206 = icmp ne i8 %205, 0
  br i1 %206, label %207, label %214, !prof !33

207:                                              ; preds = %202
  %208 = and i64 %200, 7
  %209 = trunc i64 %208 to i8
  br label %210

210:                                              ; preds = %207
  %211 = icmp sge i8 %209, %205
  br i1 %211, label %212, label %214

212:                                              ; preds = %210
  call void @__asan_report_store1(i64 %200) #8
  br label %213

213:                                              ; preds = %212
  unreachable

214:                                              ; preds = %210, %202
  store i8 %198, i8* %arrayidx22, align 1
  br label %215

215:                                              ; preds = %214
  br label %for.inc

for.inc:                                          ; preds = %215
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([13 x i32]* @__sancov_gen_.11 to i64), i64 24) to i32*)) #8
  %216 = load i32, i32* %i, align 4
  %inc = add nsw i32 %216, 1
  br label %217

217:                                              ; preds = %for.inc
  store i32 %inc, i32* %i, align 4
  br label %for.cond, !llvm.loop !34

for.end:                                          ; preds = %181
  %arrayidx23 = getelementptr inbounds [201 x i8], [201 x i8]* %21, i64 0, i64 16
  %218 = ptrtoint i8* %arrayidx23 to i64
  %219 = lshr i64 %218, 3
  %220 = add i64 %219, 2147450880
  br label %221

221:                                              ; preds = %for.end
  %222 = inttoptr i64 %220 to i8*
  %223 = load i8, i8* %222, align 1
  %224 = icmp ne i8 %223, 0
  br i1 %224, label %225, label %232, !prof !33

225:                                              ; preds = %221
  %226 = and i64 %218, 7
  %227 = trunc i64 %226 to i8
  br label %228

228:                                              ; preds = %225
  %229 = icmp sge i8 %227, %223
  br i1 %229, label %230, label %232

230:                                              ; preds = %228
  call void @__asan_report_store1(i64 %218) #8
  br label %231

231:                                              ; preds = %230
  unreachable

232:                                              ; preds = %228, %221
  store i8 0, i8* %arrayidx23, align 16
  %233 = bitcast i32* %i24 to i8*
  call void @llvm.lifetime.start.p0i8(i64 4, i8* %233) #3
  br label %234

234:                                              ; preds = %232
  store i32 0, i32* %i24, align 4
  br label %for.cond25

for.cond25:                                       ; preds = %274, %234
  %235 = load i32, i32* %i24, align 4
  call void @__sanitizer_cov_trace_const_cmp4(i32 8, i32 %235)
  br label %236

236:                                              ; preds = %for.cond25
  %cmp26 = icmp slt i32 %235, 8
  br i1 %cmp26, label %for.body28, label %for.cond.cleanup27

for.cond.cleanup27:                               ; preds = %236
  store i32 8, i32* %cleanup.dest.slot, align 4
  %237 = bitcast i32* %i24 to i8*
  br label %238

238:                                              ; preds = %for.cond.cleanup27
  call void @llvm.lifetime.end.p0i8(i64 4, i8* %237) #3
  br label %for.end37

for.body28:                                       ; preds = %236
  %239 = load i32, i32* %i24, align 4
  %add29 = add nsw i32 %239, 44
  %add30 = add nsw i32 %add29, 16
  %idxprom31 = sext i32 %add30 to i64
  %arrayidx32 = getelementptr inbounds [201 x i8], [201 x i8]* %17, i64 0, i64 %idxprom31
  %240 = ptrtoint i8* %arrayidx32 to i64
  br label %241

241:                                              ; preds = %for.body28
  %242 = lshr i64 %240, 3
  %243 = add i64 %242, 2147450880
  %244 = inttoptr i64 %243 to i8*
  %245 = load i8, i8* %244, align 1
  %246 = icmp ne i8 %245, 0
  br i1 %246, label %247, label %254, !prof !33

247:                                              ; preds = %241
  %248 = and i64 %240, 7
  %249 = trunc i64 %248 to i8
  br label %250

250:                                              ; preds = %247
  %251 = icmp sge i8 %249, %245
  br i1 %251, label %252, label %254

252:                                              ; preds = %250
  call void @__asan_report_load1(i64 %240) #8
  br label %253

253:                                              ; preds = %252
  unreachable

254:                                              ; preds = %250, %241
  %255 = load i8, i8* %arrayidx32, align 1
  %256 = load i32, i32* %i24, align 4
  %idxprom33 = sext i32 %256 to i64
  %arrayidx34 = getelementptr inbounds [201 x i8], [201 x i8]* %23, i64 0, i64 %idxprom33
  %257 = ptrtoint i8* %arrayidx34 to i64
  %258 = lshr i64 %257, 3
  br label %259

259:                                              ; preds = %254
  %260 = add i64 %258, 2147450880
  %261 = inttoptr i64 %260 to i8*
  %262 = load i8, i8* %261, align 1
  %263 = icmp ne i8 %262, 0
  br i1 %263, label %264, label %271, !prof !33

264:                                              ; preds = %259
  %265 = and i64 %257, 7
  %266 = trunc i64 %265 to i8
  br label %267

267:                                              ; preds = %264
  %268 = icmp sge i8 %266, %262
  br i1 %268, label %269, label %271

269:                                              ; preds = %267
  call void @__asan_report_store1(i64 %257) #8
  br label %270

270:                                              ; preds = %269
  unreachable

271:                                              ; preds = %267, %259
  store i8 %255, i8* %arrayidx34, align 1
  br label %272

272:                                              ; preds = %271
  br label %for.inc35

for.inc35:                                        ; preds = %272
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([13 x i32]* @__sancov_gen_.11 to i64), i64 28) to i32*)) #8
  %273 = load i32, i32* %i24, align 4
  %inc36 = add nsw i32 %273, 1
  br label %274

274:                                              ; preds = %for.inc35
  store i32 %inc36, i32* %i24, align 4
  br label %for.cond25, !llvm.loop !35

for.end37:                                        ; preds = %238
  %arrayidx38 = getelementptr inbounds [201 x i8], [201 x i8]* %23, i64 0, i64 8
  %275 = ptrtoint i8* %arrayidx38 to i64
  %276 = lshr i64 %275, 3
  %277 = add i64 %276, 2147450880
  br label %278

278:                                              ; preds = %for.end37
  %279 = inttoptr i64 %277 to i8*
  %280 = load i8, i8* %279, align 1
  %281 = icmp ne i8 %280, 0
  br i1 %281, label %282, label %289, !prof !33

282:                                              ; preds = %278
  %283 = and i64 %275, 7
  %284 = trunc i64 %283 to i8
  br label %285

285:                                              ; preds = %282
  %286 = icmp sge i8 %284, %280
  br i1 %286, label %287, label %289

287:                                              ; preds = %285
  call void @__asan_report_store1(i64 %275) #8
  br label %288

288:                                              ; preds = %287
  unreachable

289:                                              ; preds = %285, %278
  store i8 0, i8* %arrayidx38, align 8
  %290 = bitcast i32* %i39 to i8*
  call void @llvm.lifetime.start.p0i8(i64 4, i8* %290) #3
  br label %291

291:                                              ; preds = %289
  store i32 0, i32* %i39, align 4
  br label %for.cond40

for.cond40:                                       ; preds = %331, %291
  %292 = load i32, i32* %i39, align 4
  call void @__sanitizer_cov_trace_const_cmp4(i32 4, i32 %292)
  br label %293

293:                                              ; preds = %for.cond40
  %cmp41 = icmp slt i32 %292, 4
  br i1 %cmp41, label %for.body43, label %for.cond.cleanup42

for.cond.cleanup42:                               ; preds = %293
  store i32 11, i32* %cleanup.dest.slot, align 4
  %294 = bitcast i32* %i39 to i8*
  br label %295

295:                                              ; preds = %for.cond.cleanup42
  call void @llvm.lifetime.end.p0i8(i64 4, i8* %294) #3
  br label %for.end53

for.body43:                                       ; preds = %293
  %296 = load i32, i32* %i39, align 4
  %add44 = add nsw i32 %296, 44
  %add45 = add nsw i32 %add44, 16
  %add46 = add nsw i32 %add45, 8
  %idxprom47 = sext i32 %add46 to i64
  %arrayidx48 = getelementptr inbounds [201 x i8], [201 x i8]* %17, i64 0, i64 %idxprom47
  %297 = ptrtoint i8* %arrayidx48 to i64
  br label %298

298:                                              ; preds = %for.body43
  %299 = lshr i64 %297, 3
  %300 = add i64 %299, 2147450880
  %301 = inttoptr i64 %300 to i8*
  %302 = load i8, i8* %301, align 1
  %303 = icmp ne i8 %302, 0
  br i1 %303, label %304, label %311, !prof !33

304:                                              ; preds = %298
  %305 = and i64 %297, 7
  %306 = trunc i64 %305 to i8
  br label %307

307:                                              ; preds = %304
  %308 = icmp sge i8 %306, %302
  br i1 %308, label %309, label %311

309:                                              ; preds = %307
  call void @__asan_report_load1(i64 %297) #8
  br label %310

310:                                              ; preds = %309
  unreachable

311:                                              ; preds = %307, %298
  %312 = load i8, i8* %arrayidx48, align 1
  %313 = load i32, i32* %i39, align 4
  %idxprom49 = sext i32 %313 to i64
  %arrayidx50 = getelementptr inbounds [201 x i8], [201 x i8]* %25, i64 0, i64 %idxprom49
  %314 = ptrtoint i8* %arrayidx50 to i64
  %315 = lshr i64 %314, 3
  br label %316

316:                                              ; preds = %311
  %317 = add i64 %315, 2147450880
  %318 = inttoptr i64 %317 to i8*
  %319 = load i8, i8* %318, align 1
  %320 = icmp ne i8 %319, 0
  br i1 %320, label %321, label %328, !prof !33

321:                                              ; preds = %316
  %322 = and i64 %314, 7
  %323 = trunc i64 %322 to i8
  br label %324

324:                                              ; preds = %321
  %325 = icmp sge i8 %323, %319
  br i1 %325, label %326, label %328

326:                                              ; preds = %324
  call void @__asan_report_store1(i64 %314) #8
  br label %327

327:                                              ; preds = %326
  unreachable

328:                                              ; preds = %324, %316
  store i8 %312, i8* %arrayidx50, align 1
  br label %329

329:                                              ; preds = %328
  br label %for.inc51

for.inc51:                                        ; preds = %329
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([13 x i32]* @__sancov_gen_.11 to i64), i64 32) to i32*)) #8
  %330 = load i32, i32* %i39, align 4
  %inc52 = add nsw i32 %330, 1
  br label %331

331:                                              ; preds = %for.inc51
  store i32 %inc52, i32* %i39, align 4
  br label %for.cond40, !llvm.loop !36

for.end53:                                        ; preds = %295
  %arrayidx54 = getelementptr inbounds [201 x i8], [201 x i8]* %25, i64 0, i64 4
  %332 = ptrtoint i8* %arrayidx54 to i64
  %333 = lshr i64 %332, 3
  %334 = add i64 %333, 2147450880
  br label %335

335:                                              ; preds = %for.end53
  %336 = inttoptr i64 %334 to i8*
  %337 = load i8, i8* %336, align 1
  %338 = icmp ne i8 %337, 0
  br i1 %338, label %339, label %346, !prof !33

339:                                              ; preds = %335
  %340 = and i64 %332, 7
  %341 = trunc i64 %340 to i8
  br label %342

342:                                              ; preds = %339
  %343 = icmp sge i8 %341, %337
  br i1 %343, label %344, label %346

344:                                              ; preds = %342
  call void @__asan_report_store1(i64 %332) #8
  br label %345

345:                                              ; preds = %344
  unreachable

346:                                              ; preds = %342, %335
  store i8 0, i8* %arrayidx54, align 4
  %arraydecay55 = getelementptr inbounds [201 x i8], [201 x i8]* %25, i64 0, i64 0
  %call56 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ({ [4 x i8], [60 x i8] }, { [4 x i8], [60 x i8] }* @.str.9, i32 0, i32 0, i64 0), i8* %arraydecay55)
  %347 = bitcast i64* %x to i8*
  call void @llvm.lifetime.start.p0i8(i64 8, i8* %347) #3
  %arraydecay57 = getelementptr inbounds [201 x i8], [201 x i8]* %21, i64 0, i64 0
  br label %348

348:                                              ; preds = %346
  %call58 = call i64 @strtoull(i8* %arraydecay57, i8** null, i32 16) #3
  store i64 %call58, i64* %x, align 8
  %349 = load i64, i64* %x, align 8
  call void @__sanitizer_cov_trace_const_cmp8(i64 -3819410105351357762, i64 %349)
  %cmp59 = icmp ne i64 %349, -3819410105351357762
  br i1 %cmp59, label %if.then60, label %if.end61

if.then60:                                        ; preds = %348
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([13 x i32]* @__sancov_gen_.11 to i64), i64 36) to i32*)) #8
  store i32 1, i32* %retval, align 4
  br label %350

350:                                              ; preds = %if.then60
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup77

if.end61:                                         ; preds = %348
  %351 = bitcast i32* %y to i8*
  call void @llvm.lifetime.start.p0i8(i64 4, i8* %351) #3
  %arraydecay62 = getelementptr inbounds [201 x i8], [201 x i8]* %23, i64 0, i64 0
  %call63 = call i64 @strtoul(i8* %arraydecay62, i8** null, i32 16) #3
  %conv64 = trunc i64 %call63 to i32
  br label %352

352:                                              ; preds = %if.end61
  store i32 %conv64, i32* %y, align 4
  %353 = load i32, i32* %y, align 4
  call void @__sanitizer_cov_trace_const_cmp4(i32 -559038242, i32 %353)
  %cmp65 = icmp ne i32 %353, -559038242
  br i1 %cmp65, label %if.then66, label %if.end67

if.then66:                                        ; preds = %352
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([13 x i32]* @__sancov_gen_.11 to i64), i64 40) to i32*)) #8
  store i32 1, i32* %retval, align 4
  br label %354

354:                                              ; preds = %if.then66
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup76

if.end67:                                         ; preds = %352
  %355 = bitcast i16* %z to i8*
  call void @llvm.lifetime.start.p0i8(i64 2, i8* %355) #3
  %arraydecay68 = getelementptr inbounds [201 x i8], [201 x i8]* %25, i64 0, i64 0
  %call69 = call i64 @strtouq(i8* %arraydecay68, i8** null, i32 16) #3
  %conv70 = trunc i64 %call69 to i16
  store i16 %conv70, i16* %z, align 2
  br label %356

356:                                              ; preds = %if.end67
  %357 = load i16, i16* %z, align 2
  %conv71 = zext i16 %357 to i32
  %358 = zext i32 %conv71 to i64
  call void @__sanitizer_cov_trace_switch(i64 %358, i64* getelementptr inbounds ([3 x i64], [3 x i64]* @__sancov_gen_cov_switch_values.12, i32 0, i32 0))
  switch i32 %conv71, label %sw.default73 [
    i32 48879, label %sw.bb72
  ]

sw.bb72:                                          ; preds = %356
  br label %sw.epilog74

sw.default73:                                     ; preds = %356
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([13 x i32]* @__sancov_gen_.11 to i64), i64 44) to i32*)) #8
  store i32 1, i32* %retval, align 4
  br label %359

359:                                              ; preds = %sw.default73
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup

sw.epilog74:                                      ; preds = %sw.bb72
  call void @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64 ptrtoint ([13 x i32]* @__sancov_gen_.11 to i64), i64 48) to i32*)) #8
  %call75 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ({ [33 x i8], [63 x i8] }, { [33 x i8], [63 x i8] }* @.str.10, i32 0, i32 0, i64 0))
  store i32 0, i32* %retval, align 4
  br label %360

360:                                              ; preds = %sw.epilog74
  store i32 1, i32* %cleanup.dest.slot, align 4
  br label %cleanup

cleanup:                                          ; preds = %360, %359
  %361 = bitcast i16* %z to i8*
  call void @llvm.lifetime.end.p0i8(i64 2, i8* %361) #3
  br label %362

362:                                              ; preds = %cleanup
  br label %cleanup76

cleanup76:                                        ; preds = %362, %354
  %363 = bitcast i32* %y to i8*
  call void @llvm.lifetime.end.p0i8(i64 4, i8* %363) #3
  br label %364

364:                                              ; preds = %cleanup76
  br label %cleanup77

cleanup77:                                        ; preds = %364, %350
  %365 = bitcast i64* %x to i8*
  call void @llvm.lifetime.end.p0i8(i64 8, i8* %365) #3
  %366 = bitcast [201 x i8]* %25 to i8*
  %367 = add i64 %32, 118
  %368 = inttoptr i64 %367 to i64*
  store i64 -506381209866536712, i64* %368, align 1
  %369 = add i64 %32, 126
  %370 = inttoptr i64 %369 to i64*
  store i64 -506381209866536712, i64* %370, align 1
  %371 = add i64 %32, 134
  %372 = inttoptr i64 %371 to i64*
  store i64 -506381209866536712, i64* %372, align 1
  %373 = add i64 %32, 142
  %374 = inttoptr i64 %373 to i16*
  store i16 -1800, i16* %374, align 1
  call void @llvm.lifetime.end.p0i8(i64 201, i8* %366) #3
  %375 = bitcast [201 x i8]* %23 to i8*
  %376 = add i64 %32, 84
  %377 = inttoptr i64 %376 to i64*
  store i64 -506381209866536712, i64* %377, align 1
  %378 = add i64 %32, 92
  %379 = inttoptr i64 %378 to i64*
  store i64 -506381209866536712, i64* %379, align 1
  br label %380

380:                                              ; preds = %cleanup77
  %381 = add i64 %32, 100
  %382 = inttoptr i64 %381 to i64*
  store i64 -506381209866536712, i64* %382, align 1
  %383 = add i64 %32, 108
  %384 = inttoptr i64 %383 to i16*
  store i16 -1800, i16* %384, align 1
  call void @llvm.lifetime.end.p0i8(i64 201, i8* %375) #3
  %385 = bitcast [201 x i8]* %21 to i8*
  %386 = add i64 %32, 50
  %387 = inttoptr i64 %386 to i64*
  store i64 -506381209866536712, i64* %387, align 1
  %388 = add i64 %32, 58
  %389 = inttoptr i64 %388 to i64*
  store i64 -506381209866536712, i64* %389, align 1
  %390 = add i64 %32, 66
  %391 = inttoptr i64 %390 to i64*
  store i64 -506381209866536712, i64* %391, align 1
  %392 = add i64 %32, 74
  %393 = inttoptr i64 %392 to i16*
  store i16 -1800, i16* %393, align 1
  call void @llvm.lifetime.end.p0i8(i64 201, i8* %385) #3
  br label %cleanup81

cleanup81:                                        ; preds = %380, %148
  %394 = bitcast [45 x i8]* %19 to i8*
  %395 = add i64 %32, 40
  %396 = inttoptr i64 %395 to i32*
  store i32 -117901064, i32* %396, align 1
  %397 = add i64 %32, 44
  %398 = inttoptr i64 %397 to i16*
  store i16 -1800, i16* %398, align 1
  call void @llvm.lifetime.end.p0i8(i64 45, i8* %394) #3
  %399 = bitcast %struct._IO_FILE** %fp to i8*
  call void @llvm.lifetime.end.p0i8(i64 8, i8* %399) #3
  %400 = bitcast [201 x i8]* %17 to i8*
  %401 = add i64 %32, 6
  %402 = inttoptr i64 %401 to i64*
  store i64 -506381209866536712, i64* %402, align 1
  %403 = add i64 %32, 14
  %404 = inttoptr i64 %403 to i64*
  store i64 -506381209866536712, i64* %404, align 1
  %405 = add i64 %32, 22
  %406 = inttoptr i64 %405 to i64*
  br label %407

407:                                              ; preds = %cleanup81
  store i64 -506381209866536712, i64* %406, align 1
  %408 = add i64 %32, 30
  %409 = inttoptr i64 %408 to i16*
  store i16 -1800, i16* %409, align 1
  call void @llvm.lifetime.end.p0i8(i64 201, i8* %400) #3
  %410 = bitcast i8** %filename to i8*
  call void @llvm.lifetime.end.p0i8(i64 8, i8* %410) #3
  %411 = bitcast i32* %15 to i8*
  %412 = add i64 %32, 4
  %413 = inttoptr i64 %412 to i8*
  store i8 -8, i8* %413, align 1
  call void @llvm.lifetime.end.p0i8(i64 4, i8* %411) #3
  %414 = bitcast i32* %opt to i8*
  call void @llvm.lifetime.end.p0i8(i64 4, i8* %414) #3
  %415 = load i32, i32* %retval, align 4
  store i64 1172321806, i64* %26, align 8
  %416 = icmp ne i64 %7, 0
  br i1 %416, label %417, label %419

417:                                              ; preds = %407
  call void @__asan_stack_free_5(i64 %7, i64 1216)
  br label %418

418:                                              ; preds = %417
  br label %422

419:                                              ; preds = %407
  %420 = add i64 %32, 0
  call void @__asan_set_shadow_00(i64 %420, i64 152)
  br label %421

421:                                              ; preds = %419
  br label %422

422:                                              ; preds = %421, %418
  ret i32 %415
}

; Function Attrs: argmemonly nofree nosync nounwind willreturn
declare void @llvm.lifetime.start.p0i8(i64 immarg, i8* nocapture) #5

; Function Attrs: nounwind
declare dso_local i32 @getopt_long(i32, i8**, i8*, %struct.option*, i32*) #2

declare dso_local i32 @printf(i8*, ...) #1

declare dso_local %struct._IO_FILE* @fopen(i8*, i8*) #1

declare dso_local i8* @fgets(i8*, i32, %struct._IO_FILE*) #1

; Function Attrs: argmemonly nofree nosync nounwind willreturn writeonly
declare void @llvm.memset.p0i8.i64(i8* nocapture writeonly, i8, i64, i1 immarg) #6

; Function Attrs: argmemonly nofree nosync nounwind willreturn
declare void @llvm.memcpy.p0i8.p0i8.i64(i8* noalias nocapture writeonly, i8* noalias nocapture readonly, i64, i1 immarg) #5

; Function Attrs: nounwind readonly willreturn
declare dso_local i32 @memcmp(i8*, i8*, i64) #7

; Function Attrs: nounwind readonly willreturn
declare dso_local i32 @strncmp(i8*, i8*, i64) #7

; Function Attrs: nounwind readonly willreturn
declare dso_local i32 @strcmp(i8*, i8*) #7

; Function Attrs: argmemonly nofree nosync nounwind willreturn
declare void @llvm.lifetime.end.p0i8(i64 immarg, i8* nocapture) #5

; Function Attrs: nounwind
declare dso_local i64 @strtoull(i8*, i8**, i32) #2

; Function Attrs: nounwind
declare dso_local i64 @strtoul(i8*, i8**, i32) #2

; Function Attrs: nounwind
declare dso_local i64 @strtouq(i8*, i8**, i32) #2

; Function Attrs: noinline sanitize_address uwtable
define internal void @_GLOBAL__sub_I_demo.cc() #0 section ".text.startup" comdat($"_GLOBAL__sub_I_demo.cc$21576b91ab9b15712202e1b4a494877f") {
entry:
  call void @__asan_before_dynamic_init(i64 ptrtoint ([13 x i8]* @___asan_gen_.14 to i64))
  call void @__sanitizer_cov_trace_pc_guard(i32* getelementptr inbounds ([1 x i32], [1 x i32]* @__sancov_gen_.13, i32 0, i32 0)) #8
  call void @__cxx_global_var_init()
  br label %0

0:                                                ; preds = %entry
  call void @__asan_after_dynamic_init()
  ret void
}

declare void @__sanitizer_cov_trace_pc_indir(i64)

declare void @__sanitizer_cov_trace_cmp1(i8 zeroext, i8 zeroext)

declare void @__sanitizer_cov_trace_cmp2(i16 zeroext, i16 zeroext)

declare void @__sanitizer_cov_trace_cmp4(i32 zeroext, i32 zeroext)

declare void @__sanitizer_cov_trace_cmp8(i64, i64)

declare void @__sanitizer_cov_trace_const_cmp1(i8 zeroext, i8 zeroext)

declare void @__sanitizer_cov_trace_const_cmp2(i16 zeroext, i16 zeroext)

declare void @__sanitizer_cov_trace_const_cmp4(i32 zeroext, i32 zeroext)

declare void @__sanitizer_cov_trace_const_cmp8(i64, i64)

declare void @__sanitizer_cov_trace_div4(i32 zeroext)

declare void @__sanitizer_cov_trace_div8(i64)

declare void @__sanitizer_cov_trace_gep(i64)

declare void @__sanitizer_cov_trace_switch(i64, i64*)

declare void @__sanitizer_cov_trace_pc()

declare void @__sanitizer_cov_trace_pc_guard(i32*)

declare void @__sanitizer_cov_trace_pc_guard_init(i32*, i32*)

define internal void @sancov.module_ctor_trace_pc_guard() comdat {
  call void @__asan_before_dynamic_init(i64 ptrtoint ([13 x i8]* @___asan_gen_.14 to i64))
  call void @__sanitizer_cov_trace_pc_guard_init(i32* @__start___sancov_guards, i32* @__stop___sancov_guards)
  br label %1

1:                                                ; preds = %0
  call void @__asan_after_dynamic_init()
  ret void
}

declare void @__asan_report_load_n(i64, i64)

declare void @__asan_loadN(i64, i64)

declare void @__asan_report_load1(i64)

declare void @__asan_load1(i64)

declare void @__asan_report_load2(i64)

declare void @__asan_load2(i64)

declare void @__asan_report_load4(i64)

declare void @__asan_load4(i64)

declare void @__asan_report_load8(i64)

declare void @__asan_load8(i64)

declare void @__asan_report_load16(i64)

declare void @__asan_load16(i64)

declare void @__asan_report_store_n(i64, i64)

declare void @__asan_storeN(i64, i64)

declare void @__asan_report_store1(i64)

declare void @__asan_store1(i64)

declare void @__asan_report_store2(i64)

declare void @__asan_store2(i64)

declare void @__asan_report_store4(i64)

declare void @__asan_store4(i64)

declare void @__asan_report_store8(i64)

declare void @__asan_store8(i64)

declare void @__asan_report_store16(i64)

declare void @__asan_store16(i64)

declare void @__asan_report_exp_load_n(i64, i64, i32)

declare void @__asan_exp_loadN(i64, i64, i32)

declare void @__asan_report_exp_load1(i64, i32)

declare void @__asan_exp_load1(i64, i32)

declare void @__asan_report_exp_load2(i64, i32)

declare void @__asan_exp_load2(i64, i32)

declare void @__asan_report_exp_load4(i64, i32)

declare void @__asan_exp_load4(i64, i32)

declare void @__asan_report_exp_load8(i64, i32)

declare void @__asan_exp_load8(i64, i32)

declare void @__asan_report_exp_load16(i64, i32)

declare void @__asan_exp_load16(i64, i32)

declare void @__asan_report_exp_store_n(i64, i64, i32)

declare void @__asan_exp_storeN(i64, i64, i32)

declare void @__asan_report_exp_store1(i64, i32)

declare void @__asan_exp_store1(i64, i32)

declare void @__asan_report_exp_store2(i64, i32)

declare void @__asan_exp_store2(i64, i32)

declare void @__asan_report_exp_store4(i64, i32)

declare void @__asan_exp_store4(i64, i32)

declare void @__asan_report_exp_store8(i64, i32)

declare void @__asan_exp_store8(i64, i32)

declare void @__asan_report_exp_store16(i64, i32)

declare void @__asan_exp_store16(i64, i32)

declare i8* @__asan_memmove(i8*, i8*, i64)

declare i8* @__asan_memcpy(i8*, i8*, i64)

declare i8* @__asan_memset(i8*, i32, i64)

declare void @__asan_handle_no_return()

declare void @__sanitizer_ptr_cmp(i64, i64)

declare void @__sanitizer_ptr_sub(i64, i64)

declare i64 @__asan_stack_malloc_0(i64)

declare void @__asan_stack_free_0(i64, i64)

declare i64 @__asan_stack_malloc_1(i64)

declare void @__asan_stack_free_1(i64, i64)

declare i64 @__asan_stack_malloc_2(i64)

declare void @__asan_stack_free_2(i64, i64)

declare i64 @__asan_stack_malloc_3(i64)

declare void @__asan_stack_free_3(i64, i64)

declare i64 @__asan_stack_malloc_4(i64)

declare void @__asan_stack_free_4(i64, i64)

declare i64 @__asan_stack_malloc_5(i64)

declare void @__asan_stack_free_5(i64, i64)

declare i64 @__asan_stack_malloc_6(i64)

declare void @__asan_stack_free_6(i64, i64)

declare i64 @__asan_stack_malloc_7(i64)

declare void @__asan_stack_free_7(i64, i64)

declare i64 @__asan_stack_malloc_8(i64)

declare void @__asan_stack_free_8(i64, i64)

declare i64 @__asan_stack_malloc_9(i64)

declare void @__asan_stack_free_9(i64, i64)

declare i64 @__asan_stack_malloc_10(i64)

declare void @__asan_stack_free_10(i64, i64)

declare void @__asan_poison_stack_memory(i64, i64)

declare void @__asan_unpoison_stack_memory(i64, i64)

declare void @__asan_set_shadow_00(i64, i64)

declare void @__asan_set_shadow_f1(i64, i64)

declare void @__asan_set_shadow_f2(i64, i64)

declare void @__asan_set_shadow_f3(i64, i64)

declare void @__asan_set_shadow_f5(i64, i64)

declare void @__asan_set_shadow_f8(i64, i64)

declare void @__asan_alloca_poison(i64, i64)

declare void @__asan_allocas_unpoison(i64, i64)

declare void @__asan_before_dynamic_init(i64)

declare void @__asan_after_dynamic_init()

declare void @__asan_register_globals(i64, i64)

declare void @__asan_unregister_globals(i64, i64)

declare void @__asan_register_image_globals(i64)

declare void @__asan_unregister_image_globals(i64)

declare void @__asan_register_elf_globals(i64, i64, i64)

declare void @__asan_unregister_elf_globals(i64, i64, i64)

declare void @__asan_init()

define internal void @asan.module_ctor() {
  call void @__asan_init()
  call void @__asan_version_mismatch_check_v8()
  br label %1

1:                                                ; preds = %0
  call void @__asan_register_globals(i64 ptrtoint ([13 x { i64, i64, i64, i64, i64, i64, i64, i64 }]* @0 to i64), i64 13)
  ret void
}

declare void @__asan_version_mismatch_check_v8()

define internal void @asan.module_dtor() {
  call void @__asan_unregister_globals(i64 ptrtoint ([13 x { i64, i64, i64, i64, i64, i64, i64, i64 }]* @0 to i64), i64 13)
  br label %1

1:                                                ; preds = %0
  ret void
}

attributes #0 = { noinline sanitize_address uwtable "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { nounwind "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { nounwind }
attributes #4 = { noinline norecurse optnone sanitize_address uwtable mustprogress "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #5 = { argmemonly nofree nosync nounwind willreturn }
attributes #6 = { argmemonly nofree nosync nounwind willreturn writeonly }
attributes #7 = { nounwind readonly willreturn "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #8 = { nomerge }
attributes #9 = { nobuiltin nounwind readonly willreturn }
attributes #10 = { nounwind readonly willreturn }

!llvm.asan.globals = !{!3, !5, !7, !9, !11, !13, !15, !17, !19, !21, !23, !25, !27}
!llvm.module.flags = !{!29}
!llvm.ident = !{!30}

!0 = !{void ()* @__cxx_global_var_init}
!1 = !{i32 (i32, i8**)* @main}
!2 = !{void ()* @_GLOBAL__sub_I_demo.cc}
!3 = !{%"class.std::ios_base::Init"* getelementptr inbounds ({ %"class.std::ios_base::Init", [63 x i8] }, { %"class.std::ios_base::Init", [63 x i8] }* @_ZStL8__ioinit, i32 0, i32 0), !4, !"std::__ioinit", i1 true, i1 false}
!4 = !{!"/usr/lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/iostream", i32 74, i32 25}
!5 = !{[5 x i8]* getelementptr inbounds ({ [5 x i8], [59 x i8] }, { [5 x i8], [59 x i8] }* @.str, i32 0, i32 0), !6, !"<string literal>", i1 false, i1 false}
!6 = !{!"demo/demo.cc", i32 20, i32 10}
!7 = !{[1 x %struct.option]* getelementptr inbounds ({ [1 x %struct.option], [32 x i8] }, { [1 x %struct.option], [32 x i8] }* @_ZZ4mainE12long_options, i32 0, i32 0), !8, !"long_options", i1 false, i1 false}
!8 = !{!"demo/demo.cc", i32 18, i32 26}
!9 = !{[3 x i8]* getelementptr inbounds ({ [3 x i8], [61 x i8] }, { [3 x i8], [61 x i8] }* @.str.1, i32 0, i32 0), !10, !"<string literal>", i1 false, i1 false}
!10 = !{!"demo/demo.cc", i32 22, i32 42}
!11 = !{[18 x i8]* getelementptr inbounds ({ [18 x i8], [46 x i8] }, { [18 x i8], [46 x i8] }* @.str.2, i32 0, i32 0), !12, !"<string literal>", i1 false, i1 false}
!12 = !{!"demo/demo.cc", i32 31, i32 20}
!13 = !{[2 x i8]* getelementptr inbounds ({ [2 x i8], [62 x i8] }, { [2 x i8], [62 x i8] }* @.str.3, i32 0, i32 0), !14, !"<string literal>", i1 false, i1 false}
!14 = !{!"demo/demo.cc", i32 39, i32 32}
!15 = !{[27 x i8]* getelementptr inbounds ({ [27 x i8], [37 x i8] }, { [27 x i8], [37 x i8] }* @.str.4, i32 0, i32 0), !16, !"<string literal>", i1 false, i1 false}
!16 = !{!"demo/demo.cc", i32 46, i32 12}
!17 = !{[21 x i8]* getelementptr inbounds ({ [21 x i8], [43 x i8] }, { [21 x i8], [43 x i8] }* @.str.5, i32 0, i32 0), !18, !"<string literal>", i1 false, i1 false}
!18 = !{!"demo/demo.cc", i32 52, i32 28}
!19 = !{[12 x i8]* getelementptr inbounds ({ [12 x i8], [52 x i8] }, { [12 x i8], [52 x i8] }* @.str.6, i32 0, i32 0), !20, !"<string literal>", i1 false, i1 false}
!20 = !{!"demo/demo.cc", i32 53, i32 30}
!21 = !{[14 x i8]* getelementptr inbounds ({ [14 x i8], [50 x i8] }, { [14 x i8], [50 x i8] }* @.str.7, i32 0, i32 0), !22, !"<string literal>", i1 false, i1 false}
!22 = !{!"demo/demo.cc", i32 54, i32 29}
!23 = !{[27 x i8]* getelementptr inbounds ({ [27 x i8], [37 x i8] }, { [27 x i8], [37 x i8] }* @.str.8, i32 0, i32 0), !24, !"<string literal>", i1 false, i1 false}
!24 = !{!"demo/demo.cc", i32 58, i32 12}
!25 = !{[4 x i8]* getelementptr inbounds ({ [4 x i8], [60 x i8] }, { [4 x i8], [60 x i8] }* @.str.9, i32 0, i32 0), !26, !"<string literal>", i1 false, i1 false}
!26 = !{!"demo/demo.cc", i32 73, i32 12}
!27 = !{[33 x i8]* getelementptr inbounds ({ [33 x i8], [63 x i8] }, { [33 x i8], [63 x i8] }* @.str.10, i32 0, i32 0), !28, !"<string literal>", i1 false, i1 false}
!28 = !{!"demo/demo.cc", i32 95, i32 12}
!29 = !{i32 1, !"wchar_size", i32 4}
!30 = !{!"clang version 12.0.1 (git@github.com:fengzhengzhan/BTFuzz.git 0b64f5806b4302732328fa068687800669443ef8)"}
!31 = distinct !{!31, !32}
!32 = !{!"llvm.loop.mustprogress"}
!33 = !{!"branch_weights", i32 1, i32 100000}
!34 = distinct !{!34, !32}
!35 = distinct !{!35, !32}
!36 = distinct !{!36, !32}
