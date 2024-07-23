# TypeORM

> TypeORM을 하기 전에, Report의 Controller > DTO > Service 프로세스를 한번 더 정리한다.


## Report Module

```typescript
import { Module } from '@nestjs/common';
import { ReportsController } from './reports.controller';
import { ReportsService } from './reports.service';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Report } from './report.entirty'

@Module({
  imports : [TypeOrmModule.forFeature([Report])],
  controllers: [ReportsController],
  providers: [ReportsService]
})
export class ReportsModule {}

```

## Report Controller

```typescript
import { Controller, Post, Body, UseGuards } from '@nestjs/common';
import { CreateReportDto } from './dtos/create-report.dto';
import { ReportsService } from './reports.service';
import { AuthGuard } from 'src/guards/auth.guard';


@Controller('reports')
export class ReportsController {
  constructor (private reposrtService : ReportsService) {}

  @Post()
  @UseGuards(AuthGuard)
  createReport(@Body() body : CreateReportDto) {
    return this.reposrtService.create(body)
  }
}
```

## DTO(Create Dto)

```typescript
import {IsNumber, IsString, Min, Max, IsLongitude, IsLatitude} from 'class-validator'
export class CreateReportDto {
  @IsString()
  make : string;

  @IsNumber()
  @Min(0)
  @Max(1000000)
  price : number


  @IsString()
  model : string

  @IsNumber()
  @Min(1930)
  @Max(2050)
  year : number

  @IsLongitude()
  lng :number

  @IsLatitude()
  lat : number

  @IsNumber()
  @Min(0)
  @Max(1000000)
  mileage : number
}
```

## ReportService

```typescript
import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm/dist/common';
import { Repository } from 'typeorm'
import { Report } from './report.entirty';
import { CreateReportDto } from './dtos/create-report.dto';


@Injectable()
export class ReportsService {
  constructor(@InjectRepository(Report) private repo : Repository<Report>) {}

  create (reportDto : CreateReportDto) {
    const report  = this.repo.create(reportDto);
    return this.repo.save(report);
  }
}
```